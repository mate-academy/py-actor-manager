import sqlite3
from app.models import Actor
from typing import List


class ActorManager():
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(self, new_first_name: str, new_last_name: str, pk: int) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ?"
                f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = {pk}"
        )
        self._connection.commit()
