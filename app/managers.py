import sqlite3
from typing import List


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self._ensure_table()

    def _ensure_table(self):
        """Створення таблиці, якщо її немає."""
        self.connection.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
            """
        )
        self.connection.commit()

    # CREATE - C
    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    # READ - R
    def all(self) -> List:
        from models import Actor  # відкладений імпорт — уникає циклу
        cursor = self.connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor
        ]

    # UPDATE - U
    def update(self, pk: int, new_first_name: str, new_last_name: str):
        self.connection.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    # DELETE - D
    def delete(self, pk: int):
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()
