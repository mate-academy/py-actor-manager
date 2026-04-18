import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        query = f"""
        INSERT INTO {self.table_name} (first_name, last_name)
        VALUES (?, ?)
        """
        self.cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> List[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = f"""
        UPDATE {self.table_name}
        SET first_name = ?, last_name = ?
        WHERE id = ?
        """
        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (pk,))
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
