from .basic_layout import BasicLaypout 
import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from . import  utils
import datetime

class View(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QtWidgets.QApplication( sys.argv )
        self.bl = BasicLaypout()
        self.bl.budget
        
    def set_data(self, table:QtWidgets.QTableWidget, data:list[list[str]]):
        for i, row in enumerate(data):
            for j, x in enumerate(row):
                # item = QtWidgets.QTableWidgetItem(x.capitalize())
                item = QtWidgets.QTableWidgetItem(x)
                table.setItem(
                    i, j,
                    item
                )
    def update_budget(self, daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget):
        
        self.set_data(self.bl.budget.budget_table, [[str(daily), str(daily_budget)], 
                                           [str(weekly), str(weekly_budget)], 
                                           [str(monthly), str(monthly_budget)]])
        for i in range(self.bl.budget.budget_table.rowCount()): #make sum uneditable
            item = self.bl.budget.budget_table.item(i, 0)
            item.setFlags(Qt.NoItemFlags)   \
    
    def on_budget_changed(self, slot):
        self.bl.budget.budget_table.cellChanged.connect(slot)
    
    def get_new_budget(self, row, col):
        if (row, col) == (0, 1):
            return int(self.bl.budget.budget_table.item(row, col).text())
        elif (row, col) == (1, 1):
            return int(self.bl.budget.budget_table.item(row, col).text())
        elif (row, col) == (2, 1):
            return int(self.bl.budget.budget_table.item(row, col).text())
    
    def update_tree(self, categories_list):    
        items = []
        roots = []
        for category in categories_list:
            if not category[1]:
                roots.append(category)
            
            item = QtWidgets.QTreeWidgetItem([category[0]])
            items.append(item)
       
        # category.parent - 1, так как id в таблицы начинаются с единицы
        for i, category in enumerate(categories_list):
            if category[1]:
                items[category[1] - 1].addChild(items[i])

        self.bl.add_expense.tree.insertTopLevelItems(0, items)


    def on_expense_added(self, slot):
        self.bl.add_expense.add_button.clicked.connect(slot)
    
    def get_added_expense_data(self):

        date  = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        # print(self.amount_widget.text())
        amount = (self.bl.add_expense.amount_widget.text()) #TODO : check datatype
        category_name = self.bl.add_expense.tree.currentItem().text(0)
        # comment = self.bl.add_expense.comment_widget.toPlainText()
        comment = self.bl.add_expense.comment_widget.text()
        return date, amount, category_name, comment

    def get_expense_data_from_table_row(self, row):
        id = self.bl.expenses.expenses_table.item(row, 0).text()
        date = self.bl.expenses.expenses_table.item(row, 1).text()
        amount = self.bl.expenses.expenses_table.item(row, 2).text()
        category_name = self.bl.expenses.expenses_table.item(row, 3).text()
        comment = self.bl.expenses.expenses_table.item(row, 4).text()

        return id, date, amount, category_name, comment
    
    def get_expense_id_from_table_row(self, row):
        id = self.bl.expenses.expenses_table.item(row, 0).text()
        return int(id)

    def on_expense_changed(self, slot):
        self.bl.expenses.expenses_table.cellChanged.connect(slot)

    def update_expenses(self, data, slot):
        self.bl.expenses.expenses_table.setRowCount(len(data))
        self.set_data(self.bl.expenses.expenses_table, data)

        for i in range(len(data)):            
            deleteButton = QtWidgets.QPushButton("удалить")
            deleteButton.pressed.connect(lambda x = i : slot(x))
            self.bl.expenses.expenses_table.setCellWidget(i, 5, deleteButton)
            # deleteButton.clicked.connect(slot)
            
    def on_redact_category_button_clicked(self, slot):
        self.bl.add_expense.redact_category_button.clicked.connect(slot)
    
    def init_redact_category_dialog(self):
        print('in init dialog func')
        self.bl.redact_category_dialog.show()

    def on_delete_category_button_clicked(self, slot):
        self.bl.redact_category_dialog.delete_cat_button.clicked.connect(slot)

    def on_add_new_catgory_button_clicked(self, slot):
        self.bl.redact_category_dialog.add_new_cat_button.clicked.connect(slot)
