import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        is_table = self.cur.execute(f'SELECT name FROM sqlite_master WHERE name = "{self.table_name}"')
        if  is_table is None:
            self.cur.execute(f'CREATE TABEL {self.table_name}(pk, first_name, last_name)')

    def create(self, first_name, last_name):
        self.conn.execute(f'INSERT INTO {self.table_name} (first_name, last_name)'
                          ' VALUES (?, ?)',
                          (first_name, last_name))
        self.conn.commit()

    def all(self):
        self.conn.execute(f'SELECT * FROM {self.table_name}')

    def update(self, pk, new_first_name, new_last_name):
        self.conn.execute(f'UPDATE {self.table_name} '
                          'SET first_name = {new_first_name},'
                          ' last_name = {new_last_name}'
                          ' WHERE id = {pk}')
        self.conn.commit()

    def delete(self, pk):
        self.conn.execute(f'DELETE FROM {self.table_name} WHERE id = {pk}')
        self.conn.commit()