from pony.orm import *
from .base import db

class Category(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    parent = Optional(int, nullable=True)
    expenses = Set('Expense')

    @db_session
    def get_id(self):
        return self.id
    
    # @db_session
    # def reassign_category(self, new_c_id):
    #     # self.id = Category[new_c_id].id
    #     self.name = Category[new_c_id].name
    #     self.parent = Category[new_c_id].parent
    @db_session
    def get_category_by_id(c_id):
        return Category[c_id]
    
    @db_session
    def assign_new_parent(self, c_new_parent_id):
        self.parent = c_new_parent_id
    
    @db_session
    def rename_category(c_id, new_name):
        Category[c_id].name = new_name

    @db_session
    def get_category_parent(c_id):
        return Category[c_id].parent
    
    @db_session  
    def get_c_name(c_id):
        return Category[c_id].name

    @db_session
    def get_category_children( c_id):
        return Category.select(lambda c: c.parent == c_id)
    
    @staticmethod
    @db_session
    def get_all():
        query = Category.select()
        return query[:]
    
    @db_session
    def get_all_categories_as_list():
        data = Category.select()
        return [[c.id, c.name, c.parent] for c in data]
    
    @db_session
    def add_category(c_name, c_parent):
        Category(name = c_name, parent = c_parent)
        id = Category.get_latest_category_id()
        return [id, c_name, c_parent]
        
    @db_session
    def delete_category(c_id):
        Category[c_id].delete()

    @db_session
    def get_latest_category_id():
        c_id = max(c.id for c in Category)
        return c_id