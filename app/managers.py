import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.db_name = db_name
        self._connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"INSERT INTO {self.table_name} "
                f"(first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )

    def all(self) -> list:
        cursor = self._connection.execute(f"Select * FROM {self.table_name}")
        rows = cursor.fetchall()
        return [Actor(*row) for row in rows] if rows else []

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? "
                f"WHERE id = ?",
                (new_first_name, new_last_name, pk)
            )

    def delete(self, pk: int) -> None:
        with self._connection:
            self._connection.execute(
                f"DELETE FROM {self.table_name} "
                f"WHERE id = ?",
                (pk,)
            )
