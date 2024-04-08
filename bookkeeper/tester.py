from pony.orm import *
from dirs.models_dir import model
from dirs.models_dir import db, Category, Expense

with db_session:
    c = Expense.get_all_expenses_as_list_of_str()
    # print(c)
    print(type(c[0]))
