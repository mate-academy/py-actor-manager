import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    """Manager class for handling CRUD operations on Actor objects."""

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        """Insert a new actor into the database."""
        query = f"""
        INSERT INTO {self.table_name} (first_name, last_name)
        VALUES (?, ?)
        """
        cursor = self.conn.execute(query, (first_name, last_name))
        self.conn.commit()
        return Actor(
            id=cursor.lastrowid,
            first_name=first_name,
            last_name=last_name,
        )

    def all(self) -> List[Actor]:
        """Return all actors from the database as a list of Actor objects."""
        query = f"""
        SELECT id, first_name, last_name
        FROM {self.table_name}
        """
        cursor = self.conn.execute(query)
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
        """Update an existing actor by primary key (id)."""
        query = f"""
        UPDATE {self.table_name}
        SET first_name = ?, last_name = ?
        WHERE id = ?
        """
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        """Delete an actor by primary key (id)."""
        query = f"""
        DELETE FROM {self.table_name}
        WHERE id = ?
        """
        self.conn.execute(query, (pk,))
        self.conn.commit()
