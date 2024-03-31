
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

class AddExpenseWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Добавить расход')

        self.vbox = QtWidgets.QVBoxLayout()

        self.hl1 = QtWidgets.QHBoxLayout() 
        self.hl1.addWidget(QtWidgets.QLabel('Сумма'))
        self.hl1.addWidget(QtWidgets.QLineEdit(''))

        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(['a', 'b'])
        self.hl2 = QtWidgets.QHBoxLayout()
        self.hl2.addWidget(QtWidgets.QLabel('Категория'))
        self.hl2.addWidget(self.combobox)
        self.hl2.addWidget(QtWidgets.QPushButton('Редактировать'))

        self.hl3 = QtWidgets.QHBoxLayout()
        self.hl3.addWidget(QtWidgets.QLabel('Комментарий'))
        self.hl3.addWidget(QtWidgets.QTextEdit())

        self.hl4 = QtWidgets.QHBoxLayout()
        self.hl4.addWidget(QtWidgets.QPushButton('Добавить'))

        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.hl1)
        self.vbox.addLayout(self.hl2)
        self.vbox.addLayout(self.hl3)
        self.vbox.addLayout(self.hl4)
        self.setLayout(self.vbox)