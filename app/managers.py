import sqlite3
from models import Actor

class ActorManager:
    def __init__(self, db_path="cinema.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
        """)
        self.conn.commit()

    def create(self, actor: Actor):
        self.cursor.execute(
            "INSERT INTO actors (id, first_name, last_name) VALUES (?, ?, ?)",
            (actor.id, actor.first_name, actor.last_name)
        )
        self.conn.commit()

    def all(self):
        self.cursor.execute("SELECT id, first_name, last_name FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str):
        self.cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self.conn.commit()

    def delete(self, actor_id: int):
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
