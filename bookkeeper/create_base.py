from pony.orm import *
from dirs.models_dir import model
from dirs.models_dir import db, Category, Expense
# from dirs.models_dir import budget, category, expense
# from dirs.models_dir import *
# from dirs.models_dir.expense import Expense
# import tester
import dirs.models_dir.settings as settings
import datetime


# from dirs.models_dir.model import db as db

# db.bind(**settings.db_params)
# db.generate_mapping(create_tables=True)


# db.create_tables()
# db.generate_mapping()


with db_session:   
    c = Category(name = 'All')
print('c', c.get_id()) 

with db_session:
    c1 = Category(name = 'Fooood', parent = c.id)
    e1 = Expense(date = datetime.datetime(year = 2024, month=3, day = 12), amount = 3, category = c1, comment = 'cheese')

with db_session:   
    c2 = Category(name = 'Meats', parent = c1.id)
    e2 = Expense(amount = 5, category = c2, comment = 'beef' )

# print(c2.expenses)


# tester.recalculate_budget()


# db.drop_all_tables(with_all_data = True)
