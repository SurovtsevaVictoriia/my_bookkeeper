from pony.orm import *
from ..models_dir import db, Category, Budget, Expense
# from ..models import budget, category, expense
# from ..models.base import db

from bookkeeper.dirs import settings
import datetime


db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)
