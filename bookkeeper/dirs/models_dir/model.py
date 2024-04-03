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
        pass

    @orm.db_session
    def get_all_categories(self):
        return Category.get_all()
    
    @orm.db_session
    def get_all_categories_as_list(self):
        # categories = self.get_all_categories()   
        # categories_list = []
        # for category in categories:
        #     categories_list.append(self.get_category_data(category)) 
        # # return categories_list
        data = Category.select()
        return [[c.id, c.name, c.parent] for c in data]
    
    @orm.db_session
    def get_cat_id_by_name(self, cat_name:str)->int:
        return Category.get(name = cat_name).id
    
    @orm.db_session
    def get_category_name(self, c:Category):
        return c.name
    
    @orm.db_session
    def get_category_parent(self, c:Category):
        return c.parent
    
    def get_category_id(self, c:Category):
        return c.id
    
    def get_category_data(self, c:Category):
        return [c.id, c.name, c.parent]
    
    @orm.db_session
    def add_category(self, c_name, c_parent):
        Category(name = c_name, parent = c_parent)

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
    def get_all_expenses_as_list(self):
        data = Expense.select(lambda e: 1)
        return [[str(e.id), e.date.strftime("%m-%d-%Y %H:%M:%S.%f"), str(e.amount), e.category.name, e.comment ] for e in data]
        
    @orm.db_session
    def edit_expense(self, id, date, amount, category, comment):
        Expense[id].date = date
        Expense[id].amount = amount
        Expense[id].category = category
        Expense[id].comment = comment
  



    
