from pony import orm
from dirs.models_dir import db

db.drop_all_tables(with_all_data=True)
