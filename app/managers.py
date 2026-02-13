import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name: str = db_name
        self.table_name: str = table_name
        self.connection: sqlite3.Connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        query: str = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)"
        )
        cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> List[Actor]:
        cursor: sqlite3.Cursor = self.connection.cursor()
        query: str = (
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        cursor.execute(query)
        rows = cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        query: str = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?"
        )
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        query: str = (
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?"
        )
        cursor.execute(query, (pk,))
        self.connection.commit()
