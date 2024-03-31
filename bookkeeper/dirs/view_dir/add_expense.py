
import sys
import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

from ..presenter_dir.presenter import presenter

class AddExpenseWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Добавить расход')

        self.vbox = QtWidgets.QVBoxLayout()

        self.hl1 = QtWidgets.QHBoxLayout() 
        self.amount_widget = QtWidgets.QLineEdit('')
        self.hl1.addWidget(QtWidgets.QLabel('Сумма'))
        self.hl1.addWidget(self.amount_widget)


        self.tree = QtWidgets.QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Тип"])
        self.hl2 = QtWidgets.QHBoxLayout()
        self.hl2.addWidget(QtWidgets.QLabel('Категория'))
        self.hl2.addWidget(self.tree)
        self.hl2.addWidget(QtWidgets.QPushButton('Редактировать'))

        self.hl3 = QtWidgets.QHBoxLayout()
        self.comment_widget = QtWidgets.QTextEdit()
        self.hl3.addWidget(QtWidgets.QLabel('Комментарий'))
        self.hl3.addWidget(self.comment_widget)

        # add expense
        self.hl4 = QtWidgets.QHBoxLayout()
        add_button = QtWidgets.QPushButton('Добавить')
        self.hl4.addWidget(add_button)
        add_button.clicked.connect(self.add_expense)

        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.hl1)
        self.vbox.addLayout(self.hl2)
        self.vbox.addLayout(self.hl3)
        self.vbox.addLayout(self.hl4)
        self.setLayout(self.vbox)

        self.update_tree()

    def update_tree(self):
        categories = presenter.get_categories()
        
        items = []
        roots = []
        for category in categories:
            if not category.parent:
                roots.append(category)
            
            item = QtWidgets.QTreeWidgetItem([category.name])
            items.append(item)
       
        # category.parent - 1, так как id в таблицы начинаются с единицы
        for i, category in enumerate(categories):
            if category.parent:
                items[category.parent - 1].addChild(items[i])

        self.tree.insertTopLevelItems(0, items)

    def add_expense(self):
        date  = datetime.datetime.now()
        # print(self.amount_widget.text())
        amount = int(self.amount_widget.text()) #TODO : check datatype
        amount = 15
        category_name = self.tree.currentItem().text(0)
        comment = self.comment_widget.toPlainText()
        presenter.add_expense(date, amount, category_name, comment)
        # TODO: clear cells for add item after addition
        print('add button clicked')
