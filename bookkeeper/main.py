
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

# import presenter_dir
import dirs.models_dir as models_dir
import dirs.view_dir as view_dir

from dirs import settings

db = models_dir.db 
db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


data = models_dir.expense.get_all()
print(data)
view_dir.window.start_app()
