import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.sqlite")
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS actors (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL
               )
           """)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> int:
        self.cursor.execute("INSERT INTO actors (first_name, last_name)"
                            "VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self) -> list:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, actor_id: int,
               first_name: str = None,
               last_name: str = None) -> None:
        if first_name:
            self.cursor.execute("UPDATE actors "
                                "SET first_name = ? "
                                "WHERE id = ?", (first_name, actor_id))
        if last_name:
            self.cursor.execute("UPDATE actors "
                                "SET last_name = ? "
                                "WHERE id = ?", (last_name, actor_id))
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()
