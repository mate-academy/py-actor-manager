import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name)\n"
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        actors = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in actors
        ]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "UPDATE actors\n"
            "SET first_name = ?, last_name = ?\n"
            "WHERE id = ?",
            (first_name, last_name, id)
        )
        self.conn.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()
