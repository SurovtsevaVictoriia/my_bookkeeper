
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

import presenter_dir
import models_dir
import view_dir

from . import settings

db = models_dir.db 
db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)


print('in main')
app = QtWidgets.QApplication( sys.argv )
# ex = Example() #works
# et = ExpenseTable() #works!
bl = view_dir.BasicLaypout()
# sys.exit( app.exec_() )
