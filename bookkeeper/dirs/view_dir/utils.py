import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

def set_data(table:QtWidgets.QTableWidget, data:list[list[str]]):
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            item = QtWidgets.QTableWidgetItem(x.capitalize())
            table.setItem(
                i, j,
                item
            )