import sqlite3
from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        with self._get_connection() as conn:
            conn.execute(query, (first_name, last_name))
            conn.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        with self._get_connection() as conn:
            cursor = conn.execute(query)
            rows = cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        query = f"""
            UPDATE {self.table_name} 
            SET first_name = ?, last_name = ? 
            WHERE id = ?
        """
        with self._get_connection() as conn:
            conn.execute(query, (new_first_name, new_last_name, pk))
            conn.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with self._get_connection() as conn:
            conn.execute(query, (pk,))
            conn.commit()
