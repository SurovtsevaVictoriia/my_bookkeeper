from pony.orm import *
from ..models_dir import db
from ..models_dir.model import Model
from ..models_dir import settings

class _Presenter():
    def __init__(self):
        self.model = Model()
    
    def get_categories(self):
        categories = self.model.get_categories()
        return categories
    
presenter = _Presenter()