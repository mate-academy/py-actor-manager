import sqlite3
from pathlib import Path
from typing import TypeAlias

from app.models import Actor

DBPath: TypeAlias = str | Path


class ActorsManager:
    def __init__(self, db_name: DBPath, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)

        allowed_tables = {"actors"}
        if table_name not in allowed_tables:
            raise ValueError("Invalid table name")

        self._table_name = table_name

    # --- helpers ---

    def _execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        cursor = self._connection.cursor()
        cursor.execute(query, params)
        self._connection.commit()
        return cursor

    def _select_all(self) -> list[tuple]:
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM {self._table_name}")
        return cursor.fetchall()

    # --- API ---

    def all(self) -> list[Actor]:
        return [Actor(*row) for row in self._select_all()]

    def create(self, first_name: str, last_name: str) -> None:
        self._execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )

    def delete(self, pk: int) -> None:
        self._execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (pk,)
        )

    def close(self) -> None:
        self._connection.close()
