import sys
import datetime
from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent

from . import utils
from .category_tree import CategoryTree


class EditExpenseCategoryDialog(QtWidgets.QDialog):
    """Edit Category of Existing expense (select from category tree)
    """

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Выберите категорию')
        self.vbox = QtWidgets.QVBoxLayout()

        self.tree = CategoryTree()
        self.select_button = QtWidgets.QPushButton('Выбрать')

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.tree)
        self.vbox.addWidget(self.select_button)

        self.setLayout(self.vbox)

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        return super().closeEvent(arg__1)

    def update_tree(self, categories_list):
        utils.update_category_tree_f(self.tree, categories_list)

    def get_selected_id(self):
        c_id = int(self.tree.currentItem().text(0))
        return c_id

    def on_select_cat_button_clicked(self, slot, row):
        try:
            self.select_button.clicked.disconnect()
        except Exception:
            pass
        self.select_button.clicked.connect(lambda x: slot(row))
