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
        date  = datetime.datetime.now()
        # print(self.amount_widget.text())
        amount = int(self.bl.add_expense.amount_widget.text()) #TODO : check datatype
        category_name = self.bl.add_expense.tree.currentItem().text(0)
        comment = self.bl.add_expense.comment_widget.toPlainText()
        return date, amount, category_name, comment

    

    def update_expenses(self, data, slot):
        self.bl.expenses.expenses_table.setRowCount(len(data))
        self.set_data(self.bl.expenses.expenses_table, data)

        for i in range(len(data)):            
            deleteButton = QtWidgets.QPushButton("удалить")
            self.bl.expenses.expenses_table.setCellWidget(i, 4, deleteButton)
            deleteButton.clicked.connect(slot)
            

