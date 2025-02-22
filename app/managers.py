import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('library_db.sqlite')
        self.table_name = "cinema"

    def create(self, format_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        self._connection.commit()

    def all(self):
        literature_format_cursor = self._connection.execute(
            "SELECT * FROM cinema"
        )
        return [Actor(*row) for row in literature_format_cursor]

    def update(self, id_to_update: int, new_format: str):
        self._connection.execute(
            f"UPDATE {self.table_name} SET format = ? WHERE id = ?",
            (new_format, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
