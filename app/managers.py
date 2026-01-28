import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self, db_path: str = "cinema.db") -> None:
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self.connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self.connection.commit()
        return Actor(cursor.lastrowid, first_name, last_name)

    def all(self) -> List[Actor]:
        cursor = self.connection.execute("SELECT * FROM actors")
        rows = cursor.fetchall()
        return [Actor(row["id"], row["first_name"], row["last_name"]) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id),
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.connection.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
