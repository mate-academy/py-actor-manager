import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(self.db_name)

        self._conn.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                first_name TEXT NOT NULL, \
                last_name TEXT NOT NULL)"""
        )

    def create(self, first_name: str, last_name: str) -> None:
        self._conn.execute(f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """, (first_name, last_name))

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._conn.execute(f"""
            UPDATE {self.table_name} SET first_name = ?, last_name = ?
            WHERE id = ?
            """, (new_first_name, new_last_name, pk))

    def delete(self, pk: int) -> None:
        self._conn.execute(f"""
            DELETE FROM {self.table_name} WHERE id = ?
            """, (pk,))

    def all(self) -> list[Actor]:
        cursor = self._conn.execute(f"""
            SELECT * FROM {self.table_name}
            """)
        return [Actor(*row)for row in cursor.fetchall()]
