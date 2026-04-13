import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.table_name = table_name

        # создаём таблицу если её нет
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )
        """)
        self.connection.commit()


    def create(self, first_name: str, last_name: str):
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()


    def all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()

        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]


    def update(self, pk: int, new_first_name: str, new_last_name: str):
        self.cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()


    def delete(self, pk: int):
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()
