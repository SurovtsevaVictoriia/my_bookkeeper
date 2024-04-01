import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from .view_budget import BudgetTableWidget
from .view_expense import ExpenseTableWidget
from .add_expense import AddExpenseWidget
# from . import view_budget
# from . import view_expense
# from . import add_expense
# from ..presenter_dir.presenter import presenter

class BasicLaypout(QtWidgets.QWidget):
    def __init__(self):
        super(BasicLaypout, self).__init__()
        self.initUI()
        
    def closeEvent(self, event: QCloseEvent) -> None:
        # presenter.serialize_budget()
        return super().closeEvent(event)

    def initUI(self):
        verticalLayout = QtWidgets.QVBoxLayout(self)

        self.budget = BudgetTableWidget()
        self.expenses = ExpenseTableWidget()
        self.add_expense = AddExpenseWidget()

        verticalLayout.addWidget(self.budget)
        verticalLayout.addWidget(self.expenses)
        verticalLayout.addWidget(self.add_expense)

    
        self.show()
        
class Window():
    def __init__(self):
        self.app = QtWidgets.QApplication( sys.argv )
        self.bl = BasicLaypout()
        

    


def start_app():
    print('in strart app')
    
    # app = QtWidgets.QApplication( sys.argv )
    # bl = BasicLaypout()
    # sys.exit( app.exec_() )



# if __name__ == '__main__':
#     try:
#         main()
#     except Exception as e:
#         print(e.message)
if __name__ == '__main__':
    print('in window.py')
    start_app()