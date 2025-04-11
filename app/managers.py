import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_path: str = "app") -> None:
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._initialize_table()

    def _initialize_table(self) -> None:
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS actors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL)
                        """)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("INSERT INTO actors (first_name, last_name) "
                            "VALUES (?, ?)",
                            (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [
            Actor(row["id"],
                  row["first_name"],
                  row["last_name"])
            for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute("UPDATE actors SET first_name = ?, last_name = ? "
                            "WHERE id = ?",
                            (first_name, last_name, actor_id))
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?",
                            (id,))
