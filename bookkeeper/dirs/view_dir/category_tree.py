from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt

class CategoryTree(QtWidgets.QTreeWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('tree created')
        self.setColumnCount(3)
        self.setHeaderLabels("Id Категория Родитель".split())
        self.setColumnHidden(0, False)
        self.setColumnHidden(1, False)
        self.setColumnHidden(2, True)

       
    






# Try to implement maybe?
class TreeComboBox(QtWidgets.QComboBox):
    def __init__(self, *args):
        super().__init__(*args)

        self.__skip_next_hide = False

        tree_view = QtWidgets.QTreeView(self)
        tree_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        tree_view.setEditTriggers(tree_view.editTriggers())
        tree_view.setAlternatingRowColors(True)
        # tree_view.setSelectionBehavior(tree_view.SelectRows)
        tree_view.setWordWrap(True)
        tree_view.setAllColumnsShowFocus(True)
        self.setView(tree_view)

        self.view().viewport().installEventFilter(self)

    def showPopup(self):
        self.setRootModelIndex(QtCore.QModelIndex())
        super().showPopup()

    def hidePopup(self):
        self.setRootModelIndex(self.view().currentIndex().parent())
        self.setCurrentIndex(self.view().currentIndex().row())
        if self.__skip_next_hide:
            self.__skip_next_hide = False
        else:
            super().hidePopup()

    def selectIndex(self, index):
        self.setRootModelIndex(index.parent())
        self.setCurrentIndex(index.row())

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and object is self.view().viewport():
            index = self.view().indexAt(event.pos())
            self.__skip_next_hide = not self.view().visualRect(index).contains(event.pos())
        return False


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    combo = TreeComboBox()
    combo.resize(200, 30)

    parent_item = QtGui.QStandardItem('Item 1')
    parent_item.appendRow([ QtGui.QStandardItem('Child'), QtGui.QStandardItem('Yesterday')])
    model = QtGui.QStandardItemModel()
    model.appendRow([parent_item, QtGui.QStandardItem('Today')])
    model.appendRow([QtGui.QStandardItem('Item 2'), QtGui.QStandardItem('Today')])
    model.setHeaderData(0, Qt.Horizontal, 'Name', Qt.DisplayRole)
    model.setHeaderData(1, Qt.Horizontal, 'Date', Qt.DisplayRole)
    combo.setModel(model)

    combo.show()
    app.exec_()

