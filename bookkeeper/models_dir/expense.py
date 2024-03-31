from pony.orm import *
from .base import db
import datetime
from dataclasses import dataclass, field


class Expense(db.Entity):
    id = PrimaryKey(int, auto = True)
    date = Required(datetime.datetime, default = datetime.datetime.now())
    amount = Required(int)
    category = Required('Category')
    comment = Optional(str)

@db_session
def add_expense(_date, _amount, _category, _comment ):
    Expense(date = _date, amount = _amount, category = _category, comment = _comment)

@db_session
def delete_expense(_id):
    Expense[_id].delete()

@db_session
def get_all():
    data = Expense.select(lambda e: e)
    return data
    
