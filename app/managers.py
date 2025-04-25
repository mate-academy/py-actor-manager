import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self._create_table()

    def _create_table(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        """Add a new actor and return the Actor instance with assigned ID."""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

        # Get the ID of the newly created actor
        actor_id = cursor.lastrowid

        # Return the Actor instance
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, first_name, last_name FROM actors")
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor.fetchall()
        ]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
