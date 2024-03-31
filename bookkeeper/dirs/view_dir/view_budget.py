import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from . import utils
# import utils
from ..presenter_dir.presenter import presenter

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

        # self.budget_table.setEditTriggers(
        #     QtWidgets.QAbstractItemView.NoEditTriggers
        # ) #this disables editing

        

        self.header = self.budget_table.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)

        self.update_budget()
        self.budget_table.cellChanged.connect(self.on_budget_changed)
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.budget_table)
        self.setLayout(self.vbox)
    
    def update_budget(self):
        daily, weekly, monthly = presenter.calculate_expenses()
        utils.set_data(self.budget_table, [[str(daily), str(presenter.daily_budget)], 
                                           [str(weekly), str(presenter.weekly_budget)], 
                                           [str(monthly), str(presenter.monthly_budget)]])
        for i in range(self.budget_table.rowCount()): #make sum uneditable
            item = self.budget_table.item(i, 0)
            item.setFlags(Qt.NoItemFlags)
        
    def on_budget_changed(self, row, col):
        # print('changed something', row, col)
        if (row, col) == (0, 1):
            presenter.daily_budget = int(self.budget_table.item(row, col).text())
        elif (row, col) == (1, 1):
            presenter.weekly_budget = int(self.budget_table.item(row, col).text())
        elif (row, col) == (2, 1):
            presenter.monthly_budget = int(self.budget_table.item(row, col).text())



    