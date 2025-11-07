import sqlite3
from typing import List
from .models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        with self.connection:
            self.connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self.connection:
            self.connection.execute(
                f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                """,
                (first_name, last_name),
            )

    def all(self) -> List[Actor]:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()

        if not rows:
            return []

        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self.connection:
            self.connection.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (new_first_name, new_last_name, pk),
            )

    def delete(self, pk: int) -> None:
        with self.connection:
            self.connection.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (pk,),
            )

    def __del__(self) -> None:
        if hasattr(self, "connection"):
            self.connection.close()
