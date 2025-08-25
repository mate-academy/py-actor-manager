import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        with self.conn:
            self.conn.execute(f"""
                            CREATE TABLE IF NOT EXISTS {self.table_name} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT
                            )
                        """)

    def create(self, first_name, last_name):
        with self.conn:
            self.conn.execute(f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
            """, (first_name, last_name))

    def all(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, pk, new_first_name, new_last_name):
        with self.conn:
            self.conn.execute(f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """, (new_first_name, new_last_name, pk))

    def delete(self, pk):
        with self.conn:
            self.conn.execute(f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
            """, (pk,))
