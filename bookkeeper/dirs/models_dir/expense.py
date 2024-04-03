from pony.orm import *
from .base import db
import datetime
from dataclasses import dataclass, field

class Expense(db.Entity):
    id = PrimaryKey(int, auto = True)
    date = Required(datetime.datetime, default = datetime.datetime.now())
    amount = Required(float)
    category = Required('Category')
    comment = Optional(str)



