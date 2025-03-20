import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._conn = sqlite3.connect("cinema.sqlite")
        self._cursor = self._conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
        self._conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self._conn.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._cursor.execute("""
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (first_name, last_name, id))
        self._conn.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute("SELECT * FROM actors")
        actors = [
            Actor(*actor)
            for actor in self._cursor.fetchall()
        ]
        return actors

    def delete(self, id: int) -> None:
        self._cursor.execute("""
            DELETE FROM actors
            WHERE id = ?
        """, (id,))
        self._conn.commit()
