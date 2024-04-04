import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from . import utils
# import utils
# from ..presenter_dir.presenter import presenter

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

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.budget_table)

        self.setLayout(self.vbox)

    def update_budget(self, daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget):
        utils.set_data(self.budget_table, [[str(daily), str(daily_budget)], 
                                           [str(weekly), str(weekly_budget)], 
                                           [str(monthly), str(monthly_budget)]])
        for i in range(self.budget_table.rowCount()): #make sum uneditable
            item = self.budget_table.item(i, 0)
            item.setFlags(Qt.NoItemFlags)  

    def on_budget_changed(self, slot):
        self.budget_table.cellChanged.connect(slot)

    def get_new_budget(self, row, col):
        if (row, col) == (0, 1):
            return float(self.budget_table.item(row, col).text())
        elif (row, col) == (1, 1):
            return float(self.budget_table.item(row, col).text())
        elif (row, col) == (2, 1):
            return float(self.budget_table.item(row, col).text())
