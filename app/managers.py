from __future__ import annotations
from typing import Optional, Type
import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self._cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in self._cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk))

        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (pk,)
        )
        self._connection.commit()

    def __enter__(self) -> ActorManager:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[object]
    ) -> None:
        self._connection.close()
