import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> int:
        self.cursor.execute(f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """, (first_name, last_name)
                            )

        self.conn.commit()

        return self.cursor.lastrowid



