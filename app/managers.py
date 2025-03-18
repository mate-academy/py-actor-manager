import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Створення таблиці при ініціалізації, якщо вона не існує
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> int:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT id, first_name, last_name FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1],
                      last_name=row[2]) for row in rows]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id)
        )
        self.conn.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.conn.commit()

    def clear_table(self) -> None:
        # Очищення таблиці без її видалення
        self.cursor.execute("DELETE FROM actors")
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
