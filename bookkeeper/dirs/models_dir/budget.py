from pony.orm import *
from .base import db

class Budget(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    current = Required(int)
    budg = Required(int)

    


