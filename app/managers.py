import sqlite3
from models import Actor

class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def create(self, first_name, last_name):
        query = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name))
        self.connection.commit()
        return cursor.lastrowid

    def all(self):
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.execute(query)
        rows = cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, pk, new_first_name, new_last_name):
        query = f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?"
        self.connection.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(query, (pk,))
        self.connection.commit()
