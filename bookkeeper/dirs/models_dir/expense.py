"""Expense module
"""
from pony import orm
from .base import db
import datetime
from dataclasses import dataclass, field
from . import settings


class Expense(db.Entity):
    """Expense class, represents pony database table
    """
    id = orm.PrimaryKey(int, auto=True)
    date = orm.Required(datetime.datetime, default=datetime.datetime.now())
    amount = orm.Required(float)
    category = orm.Required('Category')
    comment = orm.Optional(str)

    @orm.db_session
    def get_expense_by_id(e_id: int) -> None:
        return Expense[e_id]

    @orm.db_session
    def get_expenses_in_category(c_id: int) -> orm.core.Query:
        return Expense.select(lambda e: e.category.get_id() == c_id)

    @orm.db_session
    def get_all_expenses_as_list_of_str() -> list[list[str]]:
        data = Expense.select(lambda e: 1)
        return [[str(e.id), e.date.strftime(settings.date_format), str(e.amount), str(e.category.id), e.category.name, e.comment] for e in data]

    @orm.db_session
    def reassign_category(self, new_c) -> None:
        self.category = new_c

    @orm.db_session
    def calculate_expenses() -> tuple[float, float, float]:
        today = datetime.date.today()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        todayTime = datetime.datetime(today.year, today.month, today.day)
        tomorrowTime = datetime.datetime(
            tomorrow.year, tomorrow.month, tomorrow.day+1)

        lastMonday = today + datetime.timedelta(days=-today.weekday(), weeks=0)
        lastMondayTime = datetime.datetime(
            lastMonday.year, lastMonday.month, lastMonday.day)
        firstDayTime = datetime.datetime(today.year, today.month, 1)

        daily = orm.sum(e.amount for e in Expense if e.date >
                    todayTime and e.date < tomorrowTime)
        weekly = orm.sum(e.amount for e in Expense if e.date >
                     lastMondayTime and e.date < tomorrowTime)
        monthly = orm.sum(e.amount for e in Expense if e.date >
                      firstDayTime and e.date < tomorrowTime)

        return daily, weekly, monthly

    @orm.db_session
    def add_expense(e_date, e_amount, e_category, e_comment) -> None:
        Expense(date=e_date, amount=e_amount,
                category=e_category, comment=e_comment)

    @orm.db_session
    def delete_expense(e_id: int) -> None:
        Expense[e_id].delete()

    @orm.db_session
    def edit_expense(e_id, date, amount, category, comment) -> None:
        Expense[e_id].date = date
        Expense[e_id].amount = amount
        Expense[e_id].category = category
        Expense[e_id].comment = comment
