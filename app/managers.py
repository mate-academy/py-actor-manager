import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        with self.connection:
            self.connection.execute(query)

    def create(self, first_name: str, last_name: str) -> None:
        query = f"""
        INSERT INTO {self.table_name} (first_name, last_name)
        VALUES (?, ?);
        """
        with self.connection:
            self.connection.execute(query, (first_name, last_name))

    def all(self) -> List[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        query = f"""
        UPDATE {self.table_name}
        SET first_name = ?, last_name = ?
        WHERE id = ?;
        """
        with self.connection:
            self.connection.execute(
                query, (new_first_name, new_last_name, pk)
            )

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?;"
        with self.connection:
            self.connection.execute(query, (pk,))

    def __del__(self) -> None:
        if hasattr(self, "connection"):
            self.connection.close()
