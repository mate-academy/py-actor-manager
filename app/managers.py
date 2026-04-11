import sqlite3
from pathlib import Path
from typing import TypeAlias

from app.models import Actor

DBPath: TypeAlias = str | Path


class ActorManager:
    def __init__(self, db_name: DBPath, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self._table_name = table_name

    def all(self) -> list[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM {self._table_name}")
        return [Actor(*row) for row in cursor.fetchall()]

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"INSERT INTO {self._table_name}"
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
