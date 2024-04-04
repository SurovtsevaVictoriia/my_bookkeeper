from PySide6 import QtWidgets
from . import utils

class ExpenseTableWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel('Расходы')

        self.expenses_table = QtWidgets.QTableWidget(4, 5)
        self.expenses_table.setColumnCount(7)
        self.expenses_table.setRowCount(5)
        self.expenses_table.setHorizontalHeaderLabels(
            "Id Дата Сумма  Id_Категории Категория Комментарий Удалить".split()
        )
        
        self.expenses_table.setColumnHidden(0, True)
        self.expenses_table.setColumnHidden(3, True)

        header = self.expenses_table.horizontalHeader()
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            6, QtWidgets.QHeaderView.ResizeToContents)

        # self.expenses_table.setEditTriggers(
        #     QtWidgets.QAbstractItemView.NoEditTriggers
        # ) this disables editing

        self.expenses_table.verticalHeader().hide()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.expenses_table)
        self.setLayout(self.vbox)
        # self.Update()


    def get_expense_data_from_table_row(self, row):
        id = self.expenses_table.item(row, 0).text()
        date = self.expenses_table.item(row, 1).text()
        amount = self.expenses_table.item(row, 2).text()
        category_id = self.expenses_table.item(row, 3).text()
        category_name = self.expenses_table.item(row, 4).text()
        comment = self.expenses_table.item(row, 5).text()

        return id, date, amount, category_id, category_name, comment
    
    def get_expense_id_from_table_row(self, row):
        id = self.expenses_table.item(row, 0).text()
        return int(id)

    def on_expense_changed(self, slot):
        self.expenses_table.cellChanged.connect(slot)

    def update_expenses(self, data, slot):
        self.expenses_table.setRowCount(len(data))
        utils.set_data(self.expenses_table, data)

        for i in range(len(data)):            
            deleteButton = QtWidgets.QPushButton("удалить")
            deleteButton.pressed.connect(lambda x = i : slot(x))
            self.expenses_table.setCellWidget(i, 6, deleteButton)
