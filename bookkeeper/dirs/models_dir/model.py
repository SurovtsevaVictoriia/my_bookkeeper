import datetime
from pony import orm
import json

from .base import db
from . import settings
from .category import Category 
from .expense import Expense 


db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)

class Model():
    def __init__(self):
        self.budget_filename = settings.json_name
        self.date_format = settings.date_format
    
    def get_budget_from_file(self):
        try:
            with open(self.budget_filename, 'r') as f:
                budget = json.loads(f.read())
                daily_budget = budget['daily']
                weekly_budget = budget['weekly']
                monthly_budget = budget['monthly']
        except Exception as e:
            print(e.args)
            
        else:
            return daily_budget, weekly_budget, monthly_budget
        
    @orm.db_session
    def get_all_categories_as_list(self):
        data = Category.select()
        return [[c.id, c.name, c.parent] for c in data]
        
    @orm.db_session
    def add_category(self, c_name, c_parent):
        Category(name = c_name, parent = c_parent)
        id = self.get_latest_category_id()
        return [id, c_name, c_parent]

    @orm.db_session
    def delete_category(self, c_id):
        """move all children up in the hierarchy
        """
        # move all children up in the hierarchy
        parent_id = Category[c_id].parent
        children = Category.select(lambda c: c.parent == c_id)
        #stupid way to do it, there is a relation for a reason but whatever
        expenses = Expense.select(lambda e: e.category == Category[c_id])
        if parent_id != None:
            for expense in expenses:
                expense.category = Category[parent_id]
            for child in children:
                child.parent = parent_id 
            Category[c_id].delete()
        else: 
            print('trying to delete core category')
                             
    @orm.db_session
    def rename_category(self, c_id, new_name):
        Category[c_id].name = new_name

    @orm.db_session
    def get_latest_category_id(self):
        id = orm.max(c.id for c in Category)
        return id

    @orm.db_session
    def calculate_expenses(self) -> tuple[float, float, float]:
        today = datetime.date.today()  
        tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
        todayTime = datetime.datetime(today.year, today.month, today.day)
        tomorrowTime = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day+1)

        lastMonday = today + datetime.timedelta(days=-today.weekday(), weeks = 0)
        lastMondayTime = datetime.datetime(lastMonday.year, lastMonday.month, lastMonday.day )
        firstDayTime = datetime.datetime(today.year, today.month, 1)
         
        daily = orm.sum(e.amount for e in Expense if e.date > todayTime and e.date < tomorrowTime)
        weekly = orm.sum(e.amount for e in Expense if e.date > lastMondayTime and e.date < tomorrowTime)
        monthly = orm.sum(e.amount for e in Expense if e.date > firstDayTime and e.date < tomorrowTime)

        return daily, weekly, monthly
    
    @orm.db_session
    def get_expense_id_by_params(self, e_date, e_amount, e_category, e_comment):
        return Expense.get(date = e_date, amount = e_amount, category = e_category, comment = e_comment).id

    @orm.db_session
    def add_expense(self, _date, _amount, _category, _comment ):
        Expense(date = _date, amount = _amount, category = _category, comment = _comment)

    @orm.db_session
    def delete_expense(self, e_id):
        Expense[e_id].delete()
    
    @orm.db_session
    def get_all_expenses_as_list_of_str(self):
        data = Expense.select(lambda e: 1)
        return [[str(e.id), e.date.strftime(self.date_format), str(e.amount), str(e.category.id), e.category.name, e.comment ] for e in data]
    
    def get_all_expenses_as_list(self):
        data = Expense.select()
        return [[e.id, e.date, e.amount, e.category.id, e.catgory.name, e.comment ] for e in Expense]
    
    @orm.db_session
    def edit_expense(self, e_id, date, amount, category, comment):
        Expense[e_id].date = date
        Expense[e_id].amount = amount
        Expense[e_id].category = category
        Expense[e_id].comment = comment
    
    @orm.db_session
    def edit_expense_category(self, e_id, c_id):
        Expense[e_id].category = Category[c_id]

    @orm.db_session  
    def get_c_name(self, c_id):
        return Category[c_id].name

  



    
