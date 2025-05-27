import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name, last_name):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                """,
                (first_name, last_name)
            )
            conn.commit()

    def all(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute(f"SELECT * FROM {self.table_name}")
            return [Actor(*row) for row in cursor.fetchall()]

    def update(self, pk, new_first_name, new_last_name):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (new_first_name, new_last_name, pk)
            )

    def delete(self, pk):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
                """,
                (pk,)
            )
