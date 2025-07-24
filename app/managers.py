import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._db_name = db_name
        self._table_name = table_name
        self._connection = sqlite3.Connection(self._db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?, ?);",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name};"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?;",
            (new_first_name, new_last_name, pk,)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?;",
            (pk,)
        )
        self._connection.commit()
