import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> List[Actor]:
        actors_cursor = self._connect.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name}"
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET (first_name, last_name) = (?, ?)"
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connect.commit()

    def delete(
            self,
            id_to_delete: int
    ) -> None:
        self._connect.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connect.commit()
