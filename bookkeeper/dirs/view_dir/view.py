import sys
from PySide6 import QtCore, QtWidgets
from .basic_layout import BasicLaypout


class View(QtCore.QObject):
    """
    Interface class that contains QApplication and Layout
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QtWidgets.QApplication(sys.argv)
        self.bl = BasicLaypout()

    def update_budget(self, daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget):
        self.bl.budget.update_budget(
            daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget)

    def on_budget_changed(self, slot):
        self.bl.budget.on_budget_changed(slot)

    def get_new_budget(self, row, col):
        return self.bl.budget.get_new_budget(row, col)

    def recolor_budget(self, daily, weekly, monthly,
                       daily_budget, weekly_budget, monthly_budget):
        self.bl.budget.recolor_budget(daily, weekly, monthly,
                                      daily_budget, weekly_budget, monthly_budget)

    def update_all_trees(self, categories_list):
        self.bl.add_expense.update_tree(categories_list)
        self.bl.redact_category_dialog.update_tree(categories_list)
        self.bl.edit_expense_category_dialog.update_tree(categories_list)

    def on_expense_added(self, slot):
        self.bl.add_expense.on_expense_added(slot)

    def get_added_expense_data(self):
        return self.bl.add_expense.get_added_expense_data()

    def get_expense_data_from_table_row(self, row):
        return self.bl.expenses.get_expense_data_from_table_row(row)

    def get_expense_id_from_table_row(self, row):
        return self.bl.expenses.get_expense_id_from_table_row(row)

    def on_expense_changed(self, slot):
        self.bl.expenses.on_expense_changed(slot)

    def update_expenses(self, data, slot_delete, slot_edit):
        self.bl.expenses.update_expenses(data, slot_delete, slot_edit)

    def on_redact_category_button_clicked(self, slot):
        self.bl.add_expense.on_redact_category_button_clicked(slot)

    def init_redact_category_dialog(self):
        self.bl.redact_category_dialog.exec()

    def init_edit_expense_cat_dialog(self):
        self.bl.edit_expense_category_dialog.exec()

    def on_delete_category_button_clicked(self, slot):
        self.bl.redact_category_dialog.on_delete_category_button_clicked(slot)

    def on_add_new_category_button_clicked(self, slot):
        self.bl.redact_category_dialog.on_add_new_catgory_button_clicked(slot)

    def on_rename_category_button_clicked(self, slot):
        self.bl.redact_category_dialog.on_rename_category_button_clicked(slot)

    def on_select_cat_button_clicked(self, slot, row):
        self.bl.edit_expense_category_dialog.on_select_cat_button_clicked(
            slot, row)

    def edit_expense_category(self, row, new_c_id, new_c_name, slot_edit):
        self.bl.expenses.edit_expense_category(
            row, new_c_id, new_c_name, slot_edit)

    def get_added_category_data(self):
        return self.bl.redact_category_dialog.get_added_category_data()

    def get_selected_in_redacter_category_id(self):
        return self.bl.redact_category_dialog.get_selected_id()

    def get_selected_in_expense_editor_category_id(self):
        return self.bl.edit_expense_category_dialog.get_selected_id()

    def delete_category_f(self, tree, category):
        pass
