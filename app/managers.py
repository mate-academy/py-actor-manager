import sqlite3
from typing import List
from .models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self) -> None:
        """Create table if it doesn't exist."""
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL)"
        )
        self.conn.execute(query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        """Insert a new actor and return its instance."""
        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cursor = self.conn.cursor()
        cursor.execute(query, (first_name, last_name))
        self.conn.commit()
        new_id = cursor.lastrowid
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        """Return all actors as Actor instances."""
        query = (
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """Update actor."""
        query = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        """Delete actor."""
        query = (
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?"
        )
        self.conn.execute(query, (pk,))
        self.conn.commit()
