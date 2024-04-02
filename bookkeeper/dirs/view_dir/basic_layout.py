import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from .view_budget import BudgetTableWidget
from .view_expense import ExpenseTableWidget
from .add_expense import AddExpenseWidget


class BasicLaypout(QtWidgets.QWidget):
    def __init__(self):
        super(BasicLaypout, self).__init__()
        self.initUI()
        
    def closeEvent(self, event: QCloseEvent) -> None:
        # presenter.serialize_budget()
        return super().closeEvent(event)

    def initUI(self):
        verticalLayout = QtWidgets.QVBoxLayout(self)

        self.expenses = ExpenseTableWidget()
        self.budget = BudgetTableWidget()
        self.add_expense = AddExpenseWidget()

        verticalLayout.addWidget(self.budget)
        verticalLayout.addWidget(self.expenses)
        verticalLayout.addWidget(self.add_expense)

    
        self.show()
        
