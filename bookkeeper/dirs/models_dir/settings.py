"""settings: database path, budget path, date_format
"""
db_name = '../../dirs/presenter_dir/bookkeeper_db.sqlite'
json_name = 'bookkeeper\\dirs\\presenter_dir\\budget.json'
date_format = "%d-%m-%Y %H:%M:%S.%f"
db_params = {'provider': 'sqlite', 'filename': db_name, 'create_db': True}
