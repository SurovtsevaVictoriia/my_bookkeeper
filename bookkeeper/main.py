from pony.orm import *
from models import db, Category, Budget, Expense
import settings
import datetime

db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


# db.create_tables()
# db.generate_mapping()


with db_session:   
    c = Category(name = 'All') 
    c1 = Category(name = 'Fooood', parent = c.id)
    e1 = Expense(amount = 3, category = c1, comment = 'cheese')
    c2 = Category(name = 'Meats', parent = c1.id)
    e2 = Expense(amount = 5, category = c2, comment = 'beef' )

print(c1.id)
# db.drop_all_tables(with_all_data = True)
# print(type(datetime.datetime.now()))
