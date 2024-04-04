import datetime
from pony import orm

from .base import db
from . import settings
from .category import Category 
from .expense import Expense 


db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)

class Model():
    def __init__(self):
        self.budget_filename = 'bookkeeper/dirs/presenter_dir/budget.json'        pass


    
    @orm.db_session
    def get_all_categories_as_list(self):
        data = Category.select()
        return [[c.id, c.name, c.parent] for c in data]
    
    
    @orm.db_session
    def add_category(self, c_name, c_parent):
        c = Category(name = c_name, parent = c_parent)
        id = self.get_latest_category_id()
        print('trying to return id', c_name,  id)
        return [id, c_name, c_parent]

    @orm.db_session
    def delete_category(self, id):
        """move all children up in the hierarchy
        """
        # move all children up in the hierarchy
        parent_id = Category[id].parent
        children = Category.select(lambda c: c.parent == id)
        #stupid way to do it, there is a relation for a reason but whatever
        expenses = Expense.select(lambda e: e.category == Category[id])
        for expense in expenses:
            expense.category = Category[parent_id]
        for child in children:
            child.parent = parent_id                  
        Category[id].delete()


    
    @orm.db_session
    def get_latest_category_id(self):
        id = orm.max(c.id for c in Category)
        return id

    @orm.db_session
    def calculate_expenses(self):
        now = datetime.datetime.now()
        today = datetime.date.today()   
        todayTime = datetime.datetime(today.year, today.month, today.day)
        lastMonday = today + datetime.timedelta(days=-today.weekday(), weeks = 0)
        lastMondayTime = datetime.datetime(lastMonday.year, lastMonday.month, lastMonday.day )
        firstDayTime = datetime.datetime(today.year, today.month, 1)
        print(firstDayTime, lastMondayTime, todayTime )
        
        daily = orm.sum(e.amount for e in Expense if e.date > todayTime)
        weekly = orm.sum(e.amount for e in Expense if e.date > lastMondayTime)
        monthly = orm.sum(e.amount for e in Expense if e.date > firstDayTime)

        return daily, weekly, monthly
    
    @orm.db_session
    def get_expense_id_by_params(self, e_date, e_amount, e_category, e_comment):
        return Expense.get(date = e_date, amount = e_amount, category = e_category, comment = e_comment).id

    @orm.db_session
    def add_expense(self, _date, _amount, _category, _comment ):
        Expense(date = _date, amount = _amount, category = _category, comment = _comment)

    @orm.db_session
    def delete_expense(self, _id):
        Expense[_id].delete()
    
    @orm.db_session
    def get_all_expenses_as_list_of_str(self):
        data = Expense.select(lambda e: 1)
        return [[str(e.id), e.date.strftime("%m-%d-%Y %H:%M:%S.%f"), str(e.amount), str(e.category.id), e.category.name, e.comment ] for e in data]
    
    def get_all_expenses_as_list(self):
        data = Expense.select()
        return [[e.id, e.date, e.amount, e.category.id, e.catgory.name, e.comment ] for e in Expense]
    
    @orm.db_session
    def edit_expense(self, id, date, amount, category, comment):
        Expense[id].date = date
        Expense[id].amount = amount
        Expense[id].category = category
        Expense[id].comment = comment
  



    
