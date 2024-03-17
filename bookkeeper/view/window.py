import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from view_budget import BudgetTableWidget
from view_expense import ExpenseTableWidget
from add_expense import AddExpenseWidget

class BasicLaypout(QtWidgets.QWidget):
    def __init__(self):
        super(BasicLaypout, self).__init__()
        self.initUI()

    def initUI(self):
        verticalLayout = QtWidgets.QVBoxLayout(self)

        budget = BudgetTableWidget()
        expenses = ExpenseTableWidget()
        add_expense = AddExpenseWidget()

        verticalLayout.addWidget(budget)
        verticalLayout.addWidget(expenses)
        verticalLayout.addWidget(add_expense)
    
        self.show()
        

def main():
    print('in main')
    app = QtWidgets.QApplication( sys.argv )
    # ex = Example() #works
    # et = ExpenseTable() #works!
    bl = BasicLaypout()
    sys.exit( app.exec_() )


if __name__ == '__main__':
    main()

