import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT, "
            f"last_name TEXT)"
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> int:
        cursor = self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        return cursor.lastrowid

    def all(self) -> List[Actor]:
        cursor = self.connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        rows = cursor.fetchall()
        return [
            Actor(id=row[0],
                  first_name=row[1],
                  last_name=row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        cursor = self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def delete(self, pk: int) -> bool:
        cursor = self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()
        return cursor.rowcount > 0
