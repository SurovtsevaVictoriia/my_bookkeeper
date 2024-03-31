
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

from ..presenter_dir.presenter import presenter

class AddExpenseWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Добавить расход')

        self.vbox = QtWidgets.QVBoxLayout()

        self.hl1 = QtWidgets.QHBoxLayout() 
        self.hl1.addWidget(QtWidgets.QLabel('Сумма'))
        self.hl1.addWidget(QtWidgets.QLineEdit(''))


        self.tree = QtWidgets.QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Тип"])
        self.hl2 = QtWidgets.QHBoxLayout()
        self.hl2.addWidget(QtWidgets.QLabel('Категория'))
        self.hl2.addWidget(self.tree)
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