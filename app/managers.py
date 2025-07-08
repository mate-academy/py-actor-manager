import sqlite3

from app.models import Actor


allowed_tables = ["actors", "actor"]


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        if table_name not in allowed_tables:
            raise ValueError("Invalid table name")
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        if actor_cursor:
            return [
                Actor(*row) for row in actor_cursor
            ]
        return []

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
