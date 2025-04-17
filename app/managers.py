import sqlite3
from app.models import Actor


class ActorManager():
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]

    def update(self, id_to_update: int,
               first_name_to_update: str,
               last_name_to_update: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name_to_update, last_name_to_update, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE ID = ?",
            (id_to_delete,)
        )
        self._connection.commit()
