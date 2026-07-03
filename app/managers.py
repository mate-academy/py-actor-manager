import sqlite3
from typing import List, Optional
from app.models import Actor


class ActorManager:
    """Manager class for CRUD operations on Actor table."""

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """Create table if it does not exist."""
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        """Insert new actor into table."""
        self.cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self.conn.commit()
        actor_id = self.cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        """Return all actors from table."""
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> Optional[Actor]:
        """Update actor by primary key."""
        self.cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk),
        )
        self.conn.commit()
        if self.cursor.rowcount == 0:
            return None
        return Actor(id=pk, first_name=new_first_name, last_name=new_last_name)

    def delete(self, pk: int) -> bool:
        """Delete actor by primary key."""
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (pk,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
