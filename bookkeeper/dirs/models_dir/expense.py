from pony.orm import *
from .base import db
import datetime
from dataclasses import dataclass, field
from . import settings

class Expense(db.Entity):
    id = PrimaryKey(int, auto = True)
    date = Required(datetime.datetime, default = datetime.datetime.now())
    amount = Required(float)
    category = Required('Category')
    comment = Optional(str)

    @db_session
    def get_expense_by_id(e_id):
        return Expense[e_id]

    @db_session
    def get_expenses_in_category(c_id):
        return Expense.select(lambda e: e.category.get_id() == c_id)
    
    @db_session
    def get_all_expenses_as_list_of_str():
        data = Expense.select(lambda e: 1)
        return [[str(e.id), e.date.strftime(settings.date_format), str(e.amount), str(e.category.id), e.category.name, e.comment ] for e in data]
    
    @db_session
    def reassign_category(self, new_c):
        self.category = new_c
    

    @db_session
    def calculate_expenses() -> tuple[float, float, float]:
        today = datetime.date.today()  
        tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
        todayTime = datetime.datetime(today.year, today.month, today.day)
        tomorrowTime = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day+1)

        lastMonday = today + datetime.timedelta(days=-today.weekday(), weeks = 0)
        lastMondayTime = datetime.datetime(lastMonday.year, lastMonday.month, lastMonday.day )
        firstDayTime = datetime.datetime(today.year, today.month, 1)
         
        daily = sum(e.amount for e in Expense if e.date > todayTime and e.date < tomorrowTime)
        weekly = sum(e.amount for e in Expense if e.date > lastMondayTime and e.date < tomorrowTime)
        monthly = sum(e.amount for e in Expense if e.date > firstDayTime and e.date < tomorrowTime)

        return daily, weekly, monthly
    
    @db_session
    def add_expense(e_date, e_amount, e_category, e_comment ):
        Expense(date = e_date, amount = e_amount, category = e_category, comment = e_comment)

    @db_session
    def delete_expense(e_id):
        Expense[e_id].delete()

    @db_session
    def edit_expense(e_id, date, amount, category, comment):
        Expense[e_id].date = date
        Expense[e_id].amount = amount
        Expense[e_id].category = category
        Expense[e_id].comment = comment