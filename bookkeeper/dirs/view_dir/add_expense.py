
import sys
import datetime
from PySide6 import QtWidgets
from . import utils
from .category_tree import CategoryTree

# from ..presenter_dir.presenter import presenter

class AddExpenseWidget(QtWidgets.QWidget):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Добавить расход')

        self.vbox = QtWidgets.QVBoxLayout()

        self.amount_widget = QtWidgets.QLineEdit('')
        self.hl1 = QtWidgets.QHBoxLayout() 
        self.hl1.addWidget(QtWidgets.QLabel('Сумма'))
        self.hl1.addWidget(self.amount_widget)


        self.tree = CategoryTree()

        self.hl2 = QtWidgets.QHBoxLayout()
        self.hl2.addWidget(QtWidgets.QLabel('Категория'))
        self.hl2.addWidget(self.tree)
        self.redact_category_button = QtWidgets.QPushButton('Редактировать')
        self.hl2.addWidget(self.redact_category_button)

        # self.comment_widget = QtWidgets.QTextEdit()
        self.comment_widget = QtWidgets.QLineEdit()
        self.hl3 = QtWidgets.QHBoxLayout()
        self.hl3.addWidget(QtWidgets.QLabel('Комментарий'))
        self.hl3.addWidget(self.comment_widget)

        # add expense
        self.add_button = QtWidgets.QPushButton('Добавить')
        self.hl4 = QtWidgets.QHBoxLayout()
        self.hl4.addWidget(self.add_button)
        

        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.hl1)
        self.vbox.addLayout(self.hl2)
        self.vbox.addLayout(self.hl3)
        self.vbox.addLayout(self.hl4)
        self.setLayout(self.vbox)

    def update_tree(self, categories_list):
        utils.update_category_tree_f(self.tree, categories_list)
    
    def on_expense_added(self, slot):
        self.add_button.clicked.connect(slot)

    def get_added_expense_data(self):
        date  = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        amount = float((self.amount_widget.text())) #TODO : check datatype
        category_name = self.tree.currentItem().text(1)
        category_id = int(self.tree.currentItem().text(0))
        comment = self.comment_widget.text()
        return date, amount, category_id, category_name, comment

    def on_redact_category_button_clicked(self, slot):
        self.redact_category_button.clicked.connect(slot)

