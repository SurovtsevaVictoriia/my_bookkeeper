from pony.orm import *
from .base import db

class Category(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    parent = Optional(int, nullable=True)
    expenses = Set('Expense')