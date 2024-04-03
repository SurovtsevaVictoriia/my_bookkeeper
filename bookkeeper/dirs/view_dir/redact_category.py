import sys
import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

class RedactCategory(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Что - то с категориями')
        self.vbox = QtWidgets.QVBoxLayout()
        
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Тип"])
        # выбираем родителя, а потом выбираем что делать:
        # либо добавить ребенка, либо удалить

        self.bottom_hl = QtWidgets.QHBoxLayout()
        
        self.add_vl = QtWidgets.QVBoxLayout()
        self.add_label = QtWidgets.QLabel('Добавить новую категорию')
        self.new_name_widget = QtWidgets.QLineEdit()
        self.add_new_cat_widget = QtWidgets.QPushButton('Добавить')

        self.add_vl.addWidget(self.add_label)
        self.add_vl.addWidget(self.new_name_widget)
        self.add_vl.addWidget(self.add_new_cat_widget)

        self.delete_vl = QtWidgets.QVBoxLayout()
        self.delete_label =  QtWidgets.QLabel('Удалить категорию')
        self.delete_cat_button = QtWidgets.QPushButton('Удалить')

        self.delete_vl.addWidget(self.delete_label)
        self.delete_vl.addWidget(self.delete_cat_button)

        self.bottom_hl.addLayout(self.add_vl)
        self.bottom_hl.addLayout(self.delete_vl)

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.tree)
        self.vbox.addLayout(self.bottom_hl)

        self.setLayout(self.vbox)

