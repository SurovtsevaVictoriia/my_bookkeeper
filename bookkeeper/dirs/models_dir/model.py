
from pony import orm
import json

from .base import db
from . import settings
from .category import Category
from .expense import Expense


db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


class Model():
    """Overall Model logic, including budgeting
    """

    def __init__(self):
        self.budget_filename = settings.json_name
        self.date_format = settings.date_format

    def get_budget_from_file(self):
        try:
            with open(self.budget_filename, 'r') as file:
                budget = json.loads(file.read())
                daily_budget = budget['daily']
                weekly_budget = budget['weekly']
                monthly_budget = budget['monthly']
        except Exception as e:
            with open(self.budget_filename, 'w') as file:
                data = {'daily': 1000,
                        'weekly': 5000,
                        'monthly': 15000}
                json.dump(data, file)
            return 1000,  5000,  15000
        else:
            return daily_budget, weekly_budget, monthly_budget

    def get_all_categories_as_list(self):
        return Category.get_all_categories_as_list()

    def add_category(self, c_name, c_parent):
        return Category.add_category(c_name, c_parent)

    @orm.db_session
    def delete_category(self, c_id):
        """move all children up in the hierarchy
        """
        c_parent_id = Category.get_category_parent(c_id)
        c_children = Category.get_category_children(c_id)
        # stupid way to do it, there is a relation for a reason but whatever
        expenses = Expense.get_expenses_in_category(c_id)
        if c_parent_id != None:
            for expense in expenses:
                expense.reassign_category(
                    Category.get_category_by_id(c_parent_id))
            for c_child in c_children:
                c_child.assign_new_parent(c_parent_id)

            Category.delete_category(c_id)
        else:
            print('trying to delete core category')

    def rename_category(self, c_id, new_name):
        Category.rename_category(c_id, new_name)

    def get_latest_category_id(self):
        return Category.get_latest_category_id()

    def calculate_expenses(self) -> tuple[float, float, float]:
        return Expense.calculate_expenses()

    def add_expense(self, e_date, e_amount, e_category, e_comment):
        Expense.add_expense(e_date, e_amount, e_category, e_comment)

    def delete_expense(self, e_id):
        Expense.delete_expense(e_id)

    def get_all_expenses_as_list_of_str(self):
        return Expense.get_all_expenses_as_list_of_str()

    def edit_expense(self, e_id, date, amount, category, comment):
        Expense.edit_expense(e_id, date, amount, category, comment)

    @orm.db_session
    def edit_expense_category(self, e_id, c_id):
        expense = Expense.get_expense_by_id(e_id)
        category = Category.get_category_by_id(c_id)
        expense.reassign_category(category)

    def get_c_name(self, c_id):
        return Category.get_c_name(c_id)
