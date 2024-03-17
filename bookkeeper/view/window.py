import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

# app = QtWidgets.QApplication(sys.argv)

# window = QtWidgets.QMainWindow()
# window.setWindowTitle('Bookkeeper')
# window.resize(300, 100)

# # status = QtWidgets.QStatusBar()
# # status.showMessage('Loh')
# # window.setStatusBar(status)

# central_widget = QtWidgets.QWidget()
# window.setCentralWidget(central_widget)


# vertical_layout = QtWidgets.QVBoxLayout()
# vertical_layout.addWidget(QtWidgets.QLabel('widget on v_layout'))

# # lcd = QtWidgets.QLCDNumber(11)
# # lcd.display('BRUH')
# # vertical_layout.addWidget(lcd)

# # prog_bar = QtWidgets.QProgressBar()
# # prog_bar.setValue(66)
# # prog_bar.setFormat('QprogressBar (%p%) ...')
# # prog_bar.setAlignment(Qt.AlignCenter)
# # vertical_layout.addWidget(prog_bar)

# central_widget.setLayout(vertical_layout)
# # central_widget.setToolTip('chmo') #show when cursor hovers over



# def widget_with_label(text, widget):
#     hl = QtGui.QVBoxLayout()
#     hl.addWidget(QtWidgets.QLabel(text))
#     hl.addWidget(widget)
#     return hl

# vertical_layout.addChildLayout(
#     widget_with_label('QlineEdit', 
#                       QtWidgets.QLineEdit('QLINE oneline only'))
# )
# print('hehe')

# # vertical_layout.addChildLayout(
# #     widget_with_label('QTextEdit', 
# #                       QtWidgets.QTextEdit('oneline'
# #                                           'secondline'))
# # )
# print('he')
# # vertical_layout.addChildWidget( QtWidgets.QTextEdit('oneline''secondline'))

# window.show()

# sys.exit(app.exec())

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
        expenses_table = QtWidgets.QTableWidget(4, 20)
        expenses_table.setColumnCount(4)
        expenses_table.setRowCount(20)
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

        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.addWidget(expenses_table)
        self.show()
    
def main():
    print('in main')
    app = QtWidgets.QApplication( sys.argv )
    # ex = Example() #works
    et = ExpenseTable() #works!
    sys.exit( app.exec_() )


if __name__ == '__main__':
    main()

