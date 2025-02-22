import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('Cinema')
        self.table_name = "cinema"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        literature_format_cursor = self._connection.execute(
            "SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in literature_format_cursor]

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
