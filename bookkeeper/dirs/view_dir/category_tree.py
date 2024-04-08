from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt


class CategoryTree(QtWidgets.QTreeWidget):
    """Tree of Expense Categories
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColumnCount(3)
        self.setHeaderLabels("Id Категория Родитель".split())
        self.setColumnHidden(0, False)
        self.setColumnHidden(1, False)
        self.setColumnHidden(2, True)
