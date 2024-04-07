import json

import os
import sys
import datetime

from pony.orm import *
from ..models_dir import db
from ..models_dir.model import Model


# from ..view_dir.window import  BasicLaypout
from ..view_dir.view import  View


class _Presenter():


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = Model()
        self.view = View()        
        with open(self.model.budget_filename, 'r') as f:
            budget = json.load(f)
            self.daily_budget = budget['daily']
            self.weekly_budget = budget['weekly']
            self.monthly_budget = budget['monthly'] 

        self.run()    

    
    
    def run(self) -> None:
        print('running')
        self.update_budget()
        self.update_category_tree()
        self.update_expenses()
        self.view.on_budget_changed(self.handle_on_budget_changed)
        self.view.on_expense_added(self.handle_on_expense_added)
        self.view.on_expense_changed(self.handle_on_expense_changed)
        self.view.on_redact_category_button_clicked(self.handle_on_redact_category_button_clicked)
        self.view.on_delete_category_button_clicked(self.handle_on_delete_category_button_clicked)
        self.view.on_add_new_category_button_clicked(self.handle_on_add_new_category_button_clicked)
        # self.view.on_select_cat_button_clicked(self.handle_on_select_cat_button_clicked)
        sys.exit(self.on_exit())
        
        
    def on_exit(self) -> None:
        self.view.app.exec_()
        self.serialize_budget()


    def add_default_categories(self) -> None:
        self.model.add_category('Еда' )
        self.model.add_category('Одежда')
        self.model.add_category('Мебель')
        self.model.add_category('Прочее')

    
    def add_category(self, c_name:str, c_parent_id:int) -> None:
        self.model.add_category(c_name, c_parent_id)  
    
    def serialize_budget(self) -> None:
        print('budget serialized')
        with open(self.model.budget_filename, 'w') as f:
            data = {'daily': self.daily_budget, 
                    'weekly': self.weekly_budget,
                    'monthly': self.monthly_budget}
            json.dump(data, f)    

    def update_budget(self) -> None: 
        daily, weekly, monthly = self.model.calculate_expenses()
        self.view.update_budget(daily, weekly, monthly,\
                                 self.daily_budget, self.weekly_budget, self.monthly_budget)
        print('budget updated')

    def handle_on_budget_changed(self, row:int, col:int) -> None:
        # write in presenter state
        try:
            if (row, col) == (0, 1):
                self.daily_budget = float(self.view.get_new_budget(row, col))
            elif (row, col) == (1, 1):
                self.weekly_budget = float(self.view.get_new_budget(row, col))
            elif (row, col) == (2, 1):
                self.monthly_budget = float(self.view.get_new_budget(row, col))
        except ValueError:
            print('Value Error occured')
            self.update_budget()
        else: 
            daily, weekly, monthly = self.model.calculate_expenses()
            self.view.recolor_budget(daily, weekly, monthly,\
                                 self.daily_budget, self.weekly_budget, self.monthly_budget)
    

    def update_category_tree(self) -> None:
        print('in update tree')
        categories_list = self.model.get_all_categories_as_list()
        self.view.update_all_trees(categories_list)
       

    def update_expenses(self) -> None:
        data = self.model.get_all_expenses_as_list_of_str()
        self.view.update_expenses(data, self.handle_on_delete_button_clicked, 
                                        self.handle_on_edit_expense_button_clicked)

    def handle_on_expense_added(self) -> None:
        try:
            expense_data = self.view.get_added_expense_data()      
            self.model.add_expense(*self.expense_data_to_model_data(*expense_data))
        except ValueError:
            print('empty amount')
        except AttributeError:
            print('empty category')
        else:
            self.update_expenses()
            self.update_budget()    

    def handle_on_expense_changed(self, row:int) -> None:
        try:
            new_expense_data = self.view.get_expense_data_from_table_row(row)
            # print('new expense data', new_expense_data)
            new_model_data = self.expense_data_to_model_data(*new_expense_data)
            # print('new model data', new_model_data)
        except ValueError:
            print('wrong format')
            self.update_expenses()
        else:
            self.model.edit_expense(*new_model_data )
            self.update_budget()

   

    def handle_on_delete_button_clicked(self, row:int) -> None:
        # print(row)
        print('handle dlete button clickred')
        expense_id = self.view.get_expense_id_from_table_row(row)
        self.model.delete_expense(expense_id)
        self.update_expenses()
        self.update_budget()   

    def handle_on_edit_expense_button_clicked(self, row:int) -> None:
        print(row)       
        self.view.on_select_cat_button_clicked(self.handle_on_select_cat_button_clicked, row)
        self.view.init_edit_expense_cat_dialog()
    

    def handle_on_select_cat_button_clicked(self, row)->None:
        e_id = self.view.get_expense_id_from_table_row(row)
        new_c_id = self.view.get_selected_in_expense_editor_category_id()
        new_c_name = self.model.get_c_name(new_c_id)

        self.model.edit_expense_category(e_id, new_c_id)
        self.view.edit_expense_category(row, new_c_id, new_c_name, self.handle_on_edit_expense_button_clicked)
        print('select button clicked, row = ', row, 'expense_ide ',  e_id , 'category_id ' , new_c_id )
        pass
    
        

    def handle_on_redact_category_button_clicked(self) -> None:
        print('redact category button clicked')
        self.view.init_redact_category_dialog()

    def handle_on_delete_category_button_clicked(self) -> None:
        print('delete_category_button_clicked')
        id = self.view.get_selected_in_redacter_category_id()
        self.model.delete_category(id)
        self.update_expenses()
        self.update_category_tree()
        

    def handle_on_add_new_category_button_clicked(self) -> None:
        print('add_new_catgory_button_clicked')

        try:
            name, parent_id = self.view.get_added_category_data()
        # Check database or current widget data?
        # Does it defeat the purpose of having a database?
        # print(name, parent_id)
            self.model.add_category(name, parent_id)
        except AttributeError:
            self.model.add_category('All', None)
            self.update_category_tree()
            print('everythin empty')
        except ValueError:
            print('empty name')
        else: self.update_category_tree()

        # print(name, parent_id)
    
    
    def expense_data_to_model_data_with_id(self, id:int,  date:str, amount:float, category_id:int, category_name:str, comment:str)\
                                            -> tuple[int, datetime:datetime, float, int, str]:
        print('in coverter with id')
        id = int(id)
        amount = float(amount)
        date_new = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
        category_id = int(category_id)
        # category = self.model.get_cat_id_by_name(category_name)
        return id, date_new , amount, category_id,  comment

    def expense_data_to_model_data_without_id(self,   date:str, amount:float, category_id:int, category_name:str, comment:str)\
                                            -> tuple[datetime:datetime, float, int, str] :
        print('in coverter without id')
        amount = float(amount)
        date_new = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
        category_id = int(category_id)
        # category = self.model.get_cat_id_by_name(category_name)
        return date_new , amount, category_id, comment

    def expense_data_to_model_data(self, *args) -> None:
        print(args)
        if len(args) == 5:
            return self.expense_data_to_model_data_without_id(*args)
        elif len(args) == 6:
            return self.expense_data_to_model_data_with_id(*args)




presenter = _Presenter()