from pony.orm import *
from .base import db

class Category(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    parent = Optional(int, nullable=True)
    expenses = Set('Expense')

    @db_session
    def get_id(self):
        return self.id
    
    @staticmethod
    @db_session
    def get_all():
        query = Category.select()
        return query[:]