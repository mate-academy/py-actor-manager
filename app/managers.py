import sqlite3
from dataclasses import dataclass

from app.models import Actor


@dataclass
class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
