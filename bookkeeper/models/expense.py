from pony.orm import *
from .base import db
import datetime
from dataclasses import dataclass, field

class Expense(db.Entity):
    id = PrimaryKey(int, auto = True)
    date = Required(datetime.datetime, default = datetime.datetime.now())
    amount = Required(int)
    category = Set('Category')
    comment = Optional(str)