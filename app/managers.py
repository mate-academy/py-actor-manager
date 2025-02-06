import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.create_table()

    def create_table(self) -> None:
        cursor = self._connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
        self._connection.commit()
        cursor.close()

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()
        actor_id = cursor.lastrowid
        cursor.close()
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM actors")
        rows = cursor.fetchall()
        cursor.close()
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2]) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id))
        self._connection.commit()
        cursor.close()

    def delete(self, actor_id: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self._connection.commit()
        cursor.close()
