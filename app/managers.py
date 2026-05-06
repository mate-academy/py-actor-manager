import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        if not table_name.isidentifier():
            raise ValueError("Invalid table name")

        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()
        self._table_name = table_name

        query = (
            f"CREATE TABLE IF NOT EXISTS {self._table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT, "
            "last_name TEXT)"
        )
        self._cursor.execute(query)
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"INSERT INTO {self._table_name} "
            "(first_name, last_name) VALUES (?, ?)"
        )
        self._cursor.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> List[Actor]:
        query = (
            f"SELECT id, first_name, last_name "
            f"FROM {self._table_name}"
        )
        self._cursor.execute(query)
        rows = self._cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        query = (
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self._cursor.execute(
            query,
            (new_first_name, new_last_name, pk),
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = (
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?"
        )
        self._cursor.execute(query, (pk,))
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
