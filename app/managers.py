import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"id INTEGER PRIMARY KEY, "
            f"first_name TEXT NOT NULL, "
            f"last_name TEXT NOT NULL)"
        )
        self.cursor.execute(query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)"
        )
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()
        return self.get(self.cursor.lastrowid)

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def get(self, actor_id: int) -> Actor:
        query = (
            f"SELECT * FROM {self.table_name} "
            f"WHERE id = ?"
        )
        self.cursor.execute(query, (actor_id,))
        row = self.cursor.fetchone()
        return Actor(*row) if row else None

    def update(self, pk: int, new_first_name: str, new_last_name: str):
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?"
        )
        params = (new_first_name, new_last_name, pk)
        self.cursor.execute(query, params)
        self.conn.commit()

    def delete(self, pk: int) -> bool:
        query = (
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?"
        )
        self.cursor.execute(query, (pk,))
        self.conn.commit()
        return self.cursor.rowcount > 0
