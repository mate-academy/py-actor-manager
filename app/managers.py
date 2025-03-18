import sqlite3

from models import Actor

class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('../cinema.sqlite')
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        cursor_connection = self._connection.cursor()
        cursor_connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)

        )
        self._connection.commit()


    def all(self):
        cursor_connection = self._connection.cursor()
        cursor_connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cursor_connection]

    def update(self, id_to_update: int, new_name: str, new_last_name: str):
        cursor_update = self._connection.cursor()
        cursor_update.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (new_name, new_last_name, id_to_update)
        )
        self._connection.commit()


    def delete(self, id_to_delete: int):
        cursor_delete = self._connection.cursor()
        cursor_delete.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()