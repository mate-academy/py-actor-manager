import sqlite3
from models import Actor

class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                );
            """)
            conn.commit()

    def create(self, first_name, last_name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
            """, (first_name, last_name))
            conn.commit()

    def all(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = cursor.fetchall()
            return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, pk, new_first_name, new_last_name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """, (new_first_name, new_last_name, pk))
            conn.commit()

    def delete(self, pk):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
            conn.commit()
