import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_path: str = "cinema.db") -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
        """)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> int:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?);",
            (first_name, last_name)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT id, first_name, last_name FROM actors;")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(
            self,
            actor_id: int,
            first_name: str = None,
            last_name: str = None
    ) -> None:
        updates = []
        values = []
        if first_name:
            updates.append("first_name = ?")
            values.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            values.append(last_name)
        values.append(actor_id)
        if not first_name and not last_name:
            raise ValueError

        query = (f"UPDATE actors SET {', '.join(updates)} "
                 f"WHERE id = ?")
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?;", (actor_id,))
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()
