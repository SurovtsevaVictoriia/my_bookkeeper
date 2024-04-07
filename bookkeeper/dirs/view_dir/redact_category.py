import sys
import datetime
from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent 

from . import utils
from .category_tree import CategoryTree

class RedactCategoryDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Выберите категорию')
        self.vbox = QtWidgets.QVBoxLayout()
        
        self.tree = CategoryTree()      
          
        self.bottom_hl = QtWidgets.QHBoxLayout()
        
        self.add_vl = QtWidgets.QVBoxLayout()
        self.add_label = QtWidgets.QLabel('Добавить новую категорию')
        self.new_name_widget = QtWidgets.QLineEdit()
        self.add_new_cat_button = QtWidgets.QPushButton('Добавить')

        self.add_vl.addWidget(self.add_label)
        self.add_vl.addWidget(self.new_name_widget)
        self.add_vl.addWidget(self.add_new_cat_button)

        
        self.delete_vl = QtWidgets.QVBoxLayout()
        self.delete_label =  QtWidgets.QLabel('Удалить категорию')
        self.delete_cat_button = QtWidgets.QPushButton('Удалить')

        self.rename_button = QtWidgets.QPushButton('Переименовать')

        self.delete_vl.addWidget(self.delete_label)
        self.delete_vl.addWidget(self.rename_button)
        self.delete_vl.addWidget(self.delete_cat_button)

        self.bottom_hl.addLayout(self.add_vl)
        self.bottom_hl.addLayout(self.delete_vl)

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.tree)
        self.vbox.addLayout(self.bottom_hl)

        self.setLayout(self.vbox)
    
    def closeEvent(self, arg__1: QCloseEvent) -> None:
        self.new_name_widget.setText('')
        print('dialog window cleared')
        return super().closeEvent(arg__1)

    def update_tree(self, categories_list):
        utils.update_category_tree_f(self.tree, categories_list)

    def on_delete_category_button_clicked(self, slot):
        self.delete_cat_button.clicked.connect(slot)
    
    def on_add_new_catgory_button_clicked(self, slot):
        self.add_new_cat_button.clicked.connect(slot)
    
    def on_rename_category_button_clicked(self, slot):
        self.rename_button.clicked.connect(slot)

    def get_added_category_data(self):
        name = self.new_name_widget.text()
        parent_id = int(self.tree.currentItem().text(0))
        return name, parent_id
    
    def get_selected_id(self):
        id = int(self.tree.currentItem().text(0))
        return id