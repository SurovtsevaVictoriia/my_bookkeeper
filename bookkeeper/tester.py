from pony.orm import *
from models_dir import db, Category, Budget, Expense
from models_dir import budget, category, expense
import bookkeeper.dirs.settings as settings
import datetime


db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


@db_session
def get_data(db, table_name):
    data = db.select("select * from " + table_name)
    return data

# print(get_data(db, 'Expense'))
# with db_session:
#     data = Expense.select(lambda e: e.amount > 3)
#     for e in data:
#         print(e.comment)
@db_session
def recalculate_budget():
    now = datetime.datetime.now()
    today = datetime.date.today()   
    todayTime = datetime.datetime(today.year, today.month, today.day)
    lastMonday = today + datetime.timedelta(days=today.weekday())
    lastMondayTime = datetime.datetime(lastMonday.year, lastMonday.month, lastMonday.day )
    firstDayTime = datetime.datetime(today.year, today.month, 1)
    print(firstDayTime, lastMondayTime, todayTime )
    
    daily = sum(e.amount for e in Expense if e.date > todayTime)
    weekly = sum(e.amount for e in Expense if e.date > lastMondayTime)
    monthly = sum(e.amount for e in Expense if e.date > firstDayTime)


    # Budget.get(name = "Daily").current = daily
    # Budget.get(name = "Weekly").current = weekly
    # Budget.get(name = "Monthly").current = monthly
    Budget[1].current = daily
    Budget[2].current = weekly
    Budget[3].current = monthly

# # recalculate_budget()
# with db_session:
#     print (Expense[2].category.name)

expense.add_expense(datetime.datetime.now(), 10, 2, 'shit')
expense.delete_expense(5)