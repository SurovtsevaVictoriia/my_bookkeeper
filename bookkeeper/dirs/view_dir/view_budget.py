
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from . import utils
# import utils
# from ..presenter_dir.presenter import presenter

class BudgetTableWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setBaseSize(100, 100)
        self.label = QtWidgets.QLabel('Бюджет')

        self.budget_table = QtWidgets.QTableWidget(3, 2)
        self.budget_table.setHorizontalHeaderLabels(
            "Потрачено Бюджет".split()
        )
        self.budget_table.setVerticalHeaderLabels(
            "День Неделя Месяц".split()
        )

        self.hheader = self.budget_table.horizontalHeader()
        self.hheader.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.hheader.setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        # self.header.setSectionResizeMode(            
        #     2, QtWidgets.QHeaderView.ResizeToContents)
        self.vheader = self.budget_table.verticalHeader()
        self.vheader.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.vheader.setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.vheader.setSectionResizeMode(
            2, QtWidgets.QHeaderView.Stretch)

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

        self.recolor_budget(daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget)

        
    def recolor_budget(self, daily, weekly, monthly, daily_budget, weekly_budget, monthly_budget):
        if daily > daily_budget:
            self.budget_table.item(0, 0).setBackground(Qt.red)
        else:
            self.budget_table.item(0, 0).setBackground(Qt.green)

        if weekly > weekly_budget:
            self.budget_table.item(1, 0).setBackground(Qt.red)
        else:
            self.budget_table.item(1, 0).setBackground(Qt.green)

        if monthly > monthly_budget:
            self.budget_table.item(2, 0).setBackground(Qt.red)
        else:
            self.budget_table.item(2, 0).setBackground(Qt.green)

    def on_budget_changed(self, slot):
        self.budget_table.cellChanged.connect(slot)

    def get_new_budget(self, row, col):
        if (row, col) == (0, 1):
            return self.budget_table.item(row, col).text()
        elif (row, col) == (1, 1):
            return self.budget_table.item(row, col).text()
        elif (row, col) == (2, 1):
            return self.budget_table.item(row, col).text()
