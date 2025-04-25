import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self):
        """Initialize the database connection"""
        self.connection = sqlite3.connect('cinema.db')
        self._create_table()

    def _create_table(self):
        """Create the actors table if it doesn't exist"""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        """Create a new actor record"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> List[Actor]:
        """Retrieve all actors as Actor instances"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, first_name, last_name FROM actors")
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor.fetchall()
        ]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        """Update an existing actor"""
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        """Delete an actor by ID"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.connection.commit()

    def __del__(self):
        """Close the connection when the manager is destroyed"""
        self.connection.close()