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

    set_data(budget_table, [['0', '100'],
                            ['0', '200'],
                            ['0', '1000'] ])
    return budget_table


def set_data(table:QtWidgets.QTableWidget, data:list[list[str]]):
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            table.setItem(
                i, j,
                QtWidgets.QTableWidgetItem(x.capitalize())
            )

def add_expense_layout(cats:list[str] = list(['Еда', 'Одежда'])):
    hv = QtWidgets.QVBoxLayout()

    hl1 = QtWidgets.QHBoxLayout() 
    hl1.addWidget(QtWidgets.QLabel('Сумма'))
    hl1.addWidget(QtWidgets.QLineEdit(''))


    combobox = QtWidgets.QComboBox()
    combobox.addItems(cats)
    hl2 = QtWidgets.QHBoxLayout()
    hl2.addWidget(QtWidgets.QLabel('Категория'))
    hl2.addWidget(combobox)
    hl2.addWidget(QtWidgets.QPushButton('Редактировать'))

    hl3 = QtWidgets.QHBoxLayout()
    hl3.addWidget(QtWidgets.QLabel('Комментарий'))
    hl3.addWidget(QtWidgets.QTextEdit())

    hl4 = QtWidgets.QHBoxLayout()
    hl4.addWidget(QtWidgets.QPushButton('Добавить'))


    hv.addLayout(hl1)
    hv.addLayout(hl2)
    hv.addLayout(hl3)
    hv.addLayout(hl4)
    return hv

class BasicLaypout(QtWidgets.QWidget):
    def __init__(self):
        super(BasicLaypout, self).__init__()
        self.initUI()

    def initUI(self):
        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.addWidget(expenses_table_widget())
        verticalLayout.addWidget(budget_table_widget())
        verticalLayout.addLayout(add_expense_layout())
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

