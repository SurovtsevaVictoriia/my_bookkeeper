from PySide6 import QtCore, QtGui, QtWidgets

class WidgetGallery(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(10, 3)
        col_1 = QtWidgets.QTableWidgetItem("first_col")
        col_2 =QtWidgets.QTableWidgetItem("second_col")
        deleteButton = QtWidgets.QPushButton("delete_this_row")
        deleteButton.clicked.connect(self.deleteClicked)
        for i in range(0, 10):
            deleteButton = QtWidgets.QPushButton("delete_this_row")
            deleteButton.clicked.connect(self.deleteClicked)
            self.table.setItem(i, 0, col_1)
            self.table.setItem(i, 1, col_2)
            self.table.setCellWidget(i, 2, deleteButton)
        self.mainLayout = QtWidgets.QGridLayout(self)
        self.mainLayout.addWidget(self.table)

    @QtCore.Slot()
    def deleteClicked(self):
        button = self.sender()
        print(button)
        if button:
            row = self.table.indexAt(button.pos()).row()
            print(row)
            self.table.removeRow(row)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = WidgetGallery()
    w.show()
    sys.exit(app.exec_())