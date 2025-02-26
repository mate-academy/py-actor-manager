import sqlite3
from .models import Actor


class ActorManager:
    def __init__(self, db_path="cinema.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        return Actor(id=self.cursor.lastrowid, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, actor_id: int, first_name: str = None, last_name: str = None) -> bool:
        if first_name:
            self.cursor.execute("UPDATE actors SET first_name = ? WHERE id = ?", (first_name, actor_id))
        if last_name:
            self.cursor.execute("UPDATE actors SET last_name = ? WHERE id = ?", (last_name, actor_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, actor_id: int) -> bool:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
