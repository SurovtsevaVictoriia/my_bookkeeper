from pony import orm
from dirs.models_dir import Category, Expense
import datetime

with orm.db_session:
    c = Category(name='Все категории')
print('c', c.get_id())

with orm.db_session:
    c1 = Category(name='Еда', parent=c.id)
    e1 = Expense(date=datetime.datetime(year=2024, month=3, day=12),
                 amount=3, category=c1, comment='Сыр')

with orm.db_session:
    c2 = Category(name='Одежда', parent=c1.id)
    e2 = Expense(amount=5, category=c2, comment='Куртка')

# db.drop_all_tables(with_all_data = True)
