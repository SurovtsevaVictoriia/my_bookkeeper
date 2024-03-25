from pony.orm import *
from models import db, Category, Budget, Expense
from models import budget, category, expense
import tester
import settings
import datetime

db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


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



with db_session:
    b1 = Budget( name = 'Daily', current = 0 , budg = 100)
    b2 = Budget( name = 'Weekly', current = 0 , budg = 1000)
    b3 = Budget( name = 'Monthly', current = 0 , budg = 10000)

tester.recalculate_budget()

# db.drop_all_tables(with_all_data = True)
