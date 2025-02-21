import sqlite3
import os
from models import Actor


db_path = os.path.abspath("cinema.sqlite")


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(db_path)
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)

        )
        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cursor]

    def update(
            self,
            id_to_update: int,
            new_name: str,
            new_surname: str
    ) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_name, new_surname, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
