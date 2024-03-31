from .base import db
from . import settings
from .category import Category 
from .expense import Expense 
from .budget import Budget 

db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)

class Model():
    def __init__(self):
        pass

    def get_categories(self):
        return Category.get_all()