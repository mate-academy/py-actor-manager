import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self._connection.row_factory = sqlite3.Row
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        with self._connection:
            self._connection.execute(query, (first_name, last_name))

    def all(self) -> list:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self._connection.execute(query)
        return [Actor(*row) for row in cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?"
        )
        with self._connection:
            self._connection.execute(query,
                                     (new_first_name, new_last_name, pk)
                                     )

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with self._connection:
            self._connection.execute(query, (pk,))
