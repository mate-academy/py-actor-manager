import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list:
        literary_format_cursor = self._connect.execute(
            f"SELECT first_name, last_name FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in literary_format_cursor
        ]

    def update(self, first_name: str, last_name: str, id_to_update: int) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (first_name, last_name, id_to_update)
        )
        self._connect.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connect.commit()