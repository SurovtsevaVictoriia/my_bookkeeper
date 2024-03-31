import json

import os


from pony.orm import *
from ..models_dir import db
from ..models_dir.model import Model
from ..models_dir import settings

class _Presenter():


    def __init__(self):
        self.model = Model()
        cwd = os.getcwd()
        print(cwd)
        with open('bookkeeper/dirs/presenter_dir/budget.json', 'r') as f:
            budget = json.load(f)
            self.daily_budget = budget['daily']
            self.weekly_budget = budget['weekly']
            self.monthly_budget = budget['monthly']
    
    
    def get_categories(self):
        categories = self.model.get_categories()
        return categories
    
    
    def calculate_expenses(self):
        return self.model.calculate_expenses()
    
    def serialize_budget(self):
        with open('bookkeeper/dirs/presenter_dir/budget.json', 'w') as f:
            data = {'daily': self.daily_budget, 
                    'weekly': self.weekly_budget,
                    'monthly': self.monthly_budget}
            json.dump(data, f)

    def add_expense(self, _date, _amount, _category_name, _comment):
        _category = self.model.get_cat_id_by_name(_category_name)
        self.model.add_expense(_date, _amount, _category, _comment)

    

            


    
presenter = _Presenter()