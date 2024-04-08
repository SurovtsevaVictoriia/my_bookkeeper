from pony.orm import *
from dirs.models_dir import model
from dirs.models_dir import db, Category, Expense
# from dirs.models_dir import budget, category, expense
# from dirs.models_dir import *
# from dirs.models_dir.expense import Expense
# import tester
import dirs.models_dir.settings as settings
import datetime

with db_session:   
    c = Category(name = 'Все категории')
print('c', c.get_id()) 

with db_session:
    c1 = Category(name = 'Еда', parent = c.id)
    e1 = Expense(date = datetime.datetime(year = 2024, month=3, day = 12), amount = 3, category = c1, comment = 'Сыр')

with db_session:   
    c2 = Category(name = 'Одежда', parent = c1.id)
    e2 = Expense(amount = 5, category = c2, comment = 'Куртка' )

# db.drop_all_tables(with_all_data = True)
