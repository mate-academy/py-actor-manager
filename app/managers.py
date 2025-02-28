import sqlite3
import os

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "cinema.db")

        self._connection = sqlite3.connect(db_path)
        self.name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.name}"
                                 f" (first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name,))
        self._connection.commit()

    def all(self) -> list:
        show_in_row = self._connection.execute(f"SELECT * FROM {self.name}")
        return [
            Actor(*row) for row in show_in_row
        ]

    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.name} SET first_name = ?,"
            f" last_name = ? WHERE id = ? ",
            (first_name, last_name, id_to_update))
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
