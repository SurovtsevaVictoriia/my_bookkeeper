print(f'Файл __init__.py в пакете {__name__}')
from .base import db
from . import category
from . import expense
from . import budget
from .category import Category 
from .expense import Expense 
from .budget import Budget 
