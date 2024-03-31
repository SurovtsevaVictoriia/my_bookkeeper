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

    def get_categories(self):
        return Category.get_all()
    
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
    def add_expense(self, _date, _amount, _category, _comment ):
        Expense(date = _date, amount = _amount, category = _category, comment = _comment)

    @orm.db_session
    def delete_expense(self, _id):
        Expense[_id].delete()

    @orm.db_session
    def get_cat_id_by_name(self, cat_name):
        return Category.get(name = cat_name).id
