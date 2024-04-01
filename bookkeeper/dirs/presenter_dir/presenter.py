import json

import os
import sys
import datetime
from PySide6.QtCore import Qt, QObject
from PySide6 import QtWidgets, QtCore


from pony.orm import *
from ..models_dir import db
from ..models_dir.model import Model
from ..models_dir import settings

# from ..view_dir.window import  BasicLaypout
from ..view_dir.window import  Window
from ..view_dir import  utils


class _Presenter(QtCore.QObject):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Model()
        self.window = Window()        
        
        cwd = os.getcwd()
        print(cwd)
        with open('bookkeeper/dirs/presenter_dir/budget.json', 'r') as f:
            budget = json.load(f)
            self.daily_budget = budget['daily']
            self.weekly_budget = budget['weekly']
            self.monthly_budget = budget['monthly'] 

        self.run()    

    
    
    def run(self):
        print('running')
        self.update_budget()
        self.update_tree()
        self.update_expenses()
        self.window.bl.budget.budget_table.cellChanged.connect(self.on_budget_changed)
        self.window.bl.add_expense.add_button.clicked.connect(self.add_expense)

        sys.exit( self.window.app.exec_())
        self.serialize_budget()
        

    
    def calculate_expenses(self):
        return self.model.calculate_expenses()
    
    def serialize_budget(self):
        print('budget serialized')
        with open('bookkeeper/dirs/presenter_dir/budget.json', 'w') as f:
            data = {'daily': self.daily_budget, 
                    'weekly': self.weekly_budget,
                    'monthly': self.monthly_budget}
            json.dump(data, f)    

    
    def update_budget(self):
        daily, weekly, monthly = self.calculate_expenses()
        utils.set_data(self.window.bl.budget.budget_table, [[str(daily), str(self.daily_budget)], 
                                           [str(weekly), str(self.weekly_budget)], 
                                           [str(monthly), str(self.monthly_budget)]])
        for i in range(self.window.bl.budget.budget_table.rowCount()): #make sum uneditable
            item = self.window.bl.budget.budget_table.item(i, 0)
            item.setFlags(Qt.NoItemFlags)   
        
    def on_budget_changed(self, row, col):
        # print('changed something', row, col)
        if (row, col) == (0, 1):
            self.daily_budget = int(self.window.bl.budget.budget_table.item(row, col).text())
        elif (row, col) == (1, 1):
            self.weekly_budget = int(self.window.bl.budget.budget_table.item(row, col).text())
        elif (row, col) == (2, 1):
            self.monthly_budget = int(self.window.bl.budget.budget_table.item(row, col).text())
        self.serialize_budget()#TODO: make it on window closed

    def get_categories(self):
        categories = self.model.get_categories()
        return categories
    
    def update_tree(self):
        print('in update tree')
        categories = self.get_categories()
        
        
        items = []
        roots = []
        for category in categories:
            if not category.parent:
                roots.append(category)
            
            item = QtWidgets.QTreeWidgetItem([category.name])
            items.append(item)
       
        # category.parent - 1, так как id в таблицы начинаются с единицы
        for i, category in enumerate(categories):
            if category.parent:
                items[category.parent - 1].addChild(items[i])

        self.window.bl.add_expense.tree.insertTopLevelItems(0, items)

    def update_expenses(self):
        data = self.model.get_all_expenses()
        self.window.bl.expenses.expenses_table.setRowCount(len(data))
        utils.set_data(self.window.bl.expenses.expenses_table, data)

        for i in range(len(data)):            
            deleteButton = QtWidgets.QPushButton("удалить")
            self.window.bl.expenses.expenses_table.setCellWidget(i, 4, deleteButton)
            deleteButton.clicked.connect(self.delete_clicked_expense)
            


            
            
    @QtCore.Slot()
    def delete_clicked_expense(self):
        button = self.window.bl.expenses.sender()
        button = self.sender()
        print(button)
       
        if button:
            row = self.window.bl.expenses.expenses_table.indexAt(button.pos()).row()
            print(row)

            date = self.window.bl.expenses.expenses_table.item(row, 0).text()
            date = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
            print(date)
            amount = self.window.bl.expenses.expenses_table.item(row, 1).text()
            category = self.window.bl.expenses.expenses_table.item(row, 2).text()
            category = self.model.get_cat_id_by_name(category)
            
            comment = self.window.bl.expenses.expenses_table.item(row, 3).text()

            id = self.model.get_expense_id_by_params(date, amount, category, comment)
            self.model.delete_expense(id)

            self.window.bl.expenses.expenses_table.removeRow(row)
            self.update_expenses()
            self.update_budget()

    def add_expense(self):
        date  = datetime.datetime.now()
        # print(self.amount_widget.text())
        amount = int(self.window.bl.add_expense.amount_widget.text()) #TODO : check datatype
        category_name = self.window.bl.add_expense.tree.currentItem().text(0)
        category = self.model.get_cat_id_by_name(category_name)
        comment = self.window.bl.add_expense.comment_widget.toPlainText()

        self.model.add_expense(date, amount, category, comment)
        self.update_budget()   
        self.update_expenses()   
        
        # TODO: clear cells for add item after addition
        print('add button clicked')



presenter = _Presenter()