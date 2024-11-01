import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("""
            INSERT INTO actors (first_name, last_name) VALUES (?, ?)
        """, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute("""
            UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?
        """, (first_name, last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
