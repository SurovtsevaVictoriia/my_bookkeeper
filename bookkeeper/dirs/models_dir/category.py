"""Expense Categoru module
"""
from pony import orm
from .base import db


class Category(db.Entity):
    """Category class, represents pony database table
    """
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    parent = orm.Optional(int, nullable=True)
    expenses = orm.Set('Expense')

    @orm.db_session
    def get_id(self):
        return self.id

    @orm.db_session
    def get_category_by_id(c_id: int):
        return Category[c_id]

    @orm.db_session
    def assign_new_parent(self, c_new_parent_id: int) -> None:
        self.parent = c_new_parent_id

    @orm.db_session
    def rename_category(c_id: int, new_name: str) -> None:
        Category[c_id].name = new_name

    @orm.db_session
    def get_category_parent(c_id: int) -> int:
        return Category[c_id].parent

    @orm.db_session
    def get_c_name(c_id: int) -> str:
        return Category[c_id].name

    @orm.db_session
    def get_category_children(c_id: int):
        return Category.select(lambda c: c.parent == c_id)

    @orm.db_session
    def get_all_categories_as_list() -> list:
        data = Category.select()
        return [[c.id, c.name, c.parent] for c in data]

    @orm.db_session
    def add_category(c_name: str, c_parent: int) -> list:
        Category(name=c_name, parent=c_parent)
        id = Category.get_latest_category_id()
        return [id, c_name, c_parent]

    @orm.db_session
    def delete_category(c_id: int) -> None:
        Category[c_id].delete()

    @orm.db_session
    def get_latest_category_id() -> int:
        c_id = orm.max(c.id for c in Category)
        return c_id
