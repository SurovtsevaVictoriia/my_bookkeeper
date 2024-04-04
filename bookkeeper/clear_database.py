from pony.orm import *
from dirs.models_dir import db

db.drop_all_tables(with_all_data = True)