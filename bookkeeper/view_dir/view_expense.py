
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

import os
cwd = os.getcwd()
print(cwd)
from ..models_dir.base import db
from ..models_dir import expense
import utils

class ExpenseTableWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Расходы')

        self.expenses_table = QtWidgets.QTableWidget(4, 5)
        self.expenses_table.setColumnCount(4)
        self.expenses_table.setRowCount(5)
        self.expenses_table.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split()
        )
        header = self.expenses_table.horizontalHeader()
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.ResizeToContents)
        
        # self.expenses_table.setEditTriggers(
        #     QtWidgets.QAbstractItemView.NoEditTriggers
        # ) this disables editing

        self.expenses_table.verticalHeader().hide()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.expenses_table)
        self.setLayout(self.vbox)
        self.Update()

    def Update(self):
        data = expense.get_all()
        utils.set_data(self.expenses_table, data)

        