import sys
from PySide6 import QtWidgets, QtCore

def set_data(table:QtWidgets.QTableWidget, data:list[list[str]]):
    table.blockSignals(True)
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            # item = QtWidgets.QTableWidgetItem(x.capitalize())
            item = QtWidgets.QTableWidgetItem(x)
            table.setItem(
                i, j,
                item
            )
    table.blockSignals(False)

def update_category_tree_f( tree:QtWidgets.QTreeWidget, categories_list): 
    tree.clear()   
    items = []
    roots = []
    for category in categories_list:
        print(category)
        if not category[2]:
            roots.append(category)

        # item = QtWidgets.QTreeWidgetItem(category)
        item = QtWidgets.QTreeWidgetItem([str(category[0]), 
                                            str(category[1]),
                                            str(category[2])])
        items.append(item)
        print(items)
    # category.parent - 1, так как id в таблицы начинаются с единицы
    # id могут идти не по порядку

    def is_value_at_pos(a, value, pos):
        return a[pos] == value

    def index_of_first(lst, pred, *args):
        print(*args)
        for i, v in enumerate(lst):
            if pred(v,  *args):
                return i
        return None

    for i, category in enumerate(categories_list):
        if category[2]:
            print('in tree update', i, category, category[2] - 1 )
            idx = index_of_first(categories_list, is_value_at_pos, int(category[2]), 0)
            items[idx].addChild(items[i])

    tree.insertTopLevelItems(0, items)

def add_new_category_child_f( tree:QtWidgets.QTreeWidget, category):
    item = QtWidgets.QTreeWidgetItem([str(category[0]), 
                                        str(category[1]),
                                        str(category[2])])
    print('searching for item', category)
    parent_item =  tree.findItems(str(category[0]),\
                                    flags = QtCore.Qt.MatchFlag.MatchExactly,  column = 0)[0]
    parent_item.addChild(item)
