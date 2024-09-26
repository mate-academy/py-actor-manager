import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
