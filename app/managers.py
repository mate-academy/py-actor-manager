import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.table_name = table_name
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        query = (
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?);"
        )
        cursor = self.connection.execute(query, (first_name, last_name))
        self.connection.commit()
        return Actor(
            id=cursor.lastrowid,
            first_name=first_name,
            last_name=last_name,
        )

    def all(self) -> List[Actor]:
        query = (
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name} ORDER BY id;"
        )
        cursor = self.connection.execute(query)
        rows = cursor.fetchall()
        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?;"
        )
        self.connection.execute(
            query,
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?;"
        self.connection.execute(query, (pk,))
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
