import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        title = QtWidgets.QPushButton( 'Title' )
        author = QtWidgets.QPushButton( 'Author' )
        other = QtWidgets.QPushButton( 'Other' )

        titleEdit = QtWidgets.QTextEdit()

        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.addWidget( title )
        horizontalLayout.addWidget( author )
        horizontalLayout.addWidget( other )

        verticalLayout = QtWidgets.QVBoxLayout( self )
        verticalLayout.addLayout( horizontalLayout )

        verticalLayout.addWidget( titleEdit )


        self.setLayout( verticalLayout )

        self.setGeometry( 300, 300, 350, 300 )
        self.setWindowTitle( 'Review' )
        self.show()

class ExpenseTable(QtWidgets.QWidget):
    def __init__(self):
        super(ExpenseTable, self).__init__()
        self.initUI()

    def initUI(self):        

        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.addWidget(expenses_table_widget())
        self.show()
    
def expenses_table_widget():
    expenses_table = QtWidgets.QTableWidget(4, 5)
    expenses_table.setColumnCount(4)
    expenses_table.setRowCount(5)
    expenses_table.setHorizontalHeaderLabels(
        "Дата Сумма Категория Комментарий".split()
    )
    header = expenses_table.horizontalHeader()
    header.setSectionResizeMode(
        0, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(
        1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(
        2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(
        3, QtWidgets.QHeaderView.ResizeToContents)
    
    # expenses_table.setEditTriggers(
    #     QtWidgets.QAbstractItemView.NoEditTriggers
    # ) this disables editing

    expenses_table.verticalHeader().hide()
    return expenses_table
def budget_table_widget():
    budget_table = QtWidgets.QTableWidget(3, 2)
    budget_table.setHorizontalHeaderLabels(
        "Потрачено Бюджет".split()
    )
    budget_table.setVerticalHeaderLabels(
        "День Неделя Месяц".split()
    )
    header = budget_table.horizontalHeader()
    header.setSectionResizeMode(
        0, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(
        1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(
        2, QtWidgets.QHeaderView.ResizeToContents)

    return budget_table

class BasicLaypout(QtWidgets.QWidget):
    def __init__(self):
        super(BasicLaypout, self).__init__()
        self.initUI()

    def initUI(self):
        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.addWidget(expenses_table_widget())
        verticalLayout.addWidget(budget_table_widget())
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

