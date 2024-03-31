import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import utils


class BudgetTableWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = QtWidgets.QLabel('Бюджет')
        
        self.budget_table = QtWidgets.QTableWidget(3, 2)
        self.budget_table.setHorizontalHeaderLabels(
            "Потрачено Бюджет".split()
        )
        self.budget_table.setVerticalHeaderLabels(
            "День Неделя Месяц".split()
        )
        self.header = self.budget_table.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)

        utils.set_data(self.budget_table, [['0', '100'],
                                ['0', '200'],
                                ['0', '1000'] ])
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.budget_table)
        self.setLayout(self.vbox)
    
    