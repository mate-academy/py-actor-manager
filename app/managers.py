import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._db_name = db_name
        self._table_name = table_name
        self._connector = sqlite3.connect(self._db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connector.execute(
            f"INSERT INTO {self._table_name} "
            "(first_name, last_name) VALUES (?, ?);",
            (first_name, last_name)
        )
        self._connector.commit()

    def all(self) -> list:
        cursor = self._connector.execute(
            "SELECT * "
            f"FROM {self._table_name};"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connector.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?;",
            (new_first_name, new_last_name, pk)
        )
        self._connector.commit()

    def delete(self, pk: int) -> None:
        self._connector.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?;",
            (pk,)
        )
        self._connector.commit()

    def __del__(self) -> None:
        self._connector.close()
