import json

import os
import sys
import datetime

from pony.orm import *
from ..models_dir import db
from ..models_dir.model import Model
from ..models_dir import settings

# from ..view_dir.window import  BasicLaypout
from ..view_dir.view import  View
from ..view_dir import  utils


class _Presenter():


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Model()
        self.view = View()        
        
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
        self.view.on_budget_changed(self.handle_on_budget_changed)
        self.view.on_expense_added(self.handle_expense_added)


        sys.exit( self.view.app.exec_())
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

    # has qt DONE
    def update_budget(self): 
        daily, weekly, monthly = self.calculate_expenses()
        self.view.update_budget(daily, weekly, monthly, self.daily_budget, self.weekly_budget, self.monthly_budget)

    # has qt  DONE
    def handle_on_budget_changed(self, row, col):
        # print('changed something', row, col)
        if (row, col) == (0, 1):
            self.daily_budget = self.view.get_new_budget(row, col)
        elif (row, col) == (1, 1):
            self.weekly_budget = self.view.get_new_budget(row, col)
        elif (row, col) == (2, 1):
            self.monthly_budget = self.view.get_new_budget(row, col)
        self.serialize_budget()#TODO: make it on window closed

    def get_categories(self):
        categories = self.model.get_categories()
        return categories
    
    # has qt DONE
    def update_tree(self):
        print('in update tree')
        categories = self.get_categories()   
        categories_list = []
        for category in categories:
            categories_list.append([category.name, category.parent])     

        self.view.update_tree(categories_list)
    


    
    def update_expenses(self):
        data = self.model.get_all_expenses()
        self.view.update_expenses(data, self.handle_delete_button_clicked)

    def handle_expense_added(self):
        expense_data = self.view.get_added_expense_data()
      
        self.model.add_expense(*self.expense_data_to_model_data(*expense_data))
        self.update_expenses()
        self.update_budget()
    
    def expense_data_to_model_data(self, date, amount, category_name, comment):
        # date_new = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
        category = self.model.get_cat_id_by_name(category_name)
        return date , amount, category, comment
    

    def handle_delete_button_clicked(self):
        
        print('handle dlete button clickred')
        button = self.view.sender()
        print(button)

    # has qt
   
    def delete_clicked_expense(self, x):

        button = self.sender()
        button = x
        print(button)
       
        if button:
            row = self.view.bl.expenses.expenses_table.indexAt(button.pos()).row()
            print(row)

            date = self.view.bl.expenses.expenses_table.item(row, 0).text()
            date = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
            print(date)
            amount = self.view.bl.expenses.expenses_table.item(row, 1).text()
            category = self.view.bl.expenses.expenses_table.item(row, 2).text()
            category = self.model.get_cat_id_by_name(category)

            comment = self.view.bl.expenses.expenses_table.item(row, 3).text()

            id = self.model.get_expense_id_by_params(date, amount, category, comment)
            self.model.delete_expense(id)

            self.view.bl.expenses.expenses_table.removeRow(row)
            self.update_expenses()
            self.update_budget()

  



presenter = _Presenter()