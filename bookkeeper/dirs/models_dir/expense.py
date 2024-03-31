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
def get_all():
    data = Expense.select(lambda e: 1)
    return [[e.date.strftime("%m/%d/%Y, %H:%M:%S"), str(e.amount), e.category.name, e.comment ] for e in data]