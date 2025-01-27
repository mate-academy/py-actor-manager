import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, new_first_name, new_last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name } (first_name, last_name) VALUES (?, ?)",
            (new_first_name, new_last_name)
        )
        self._connection.commit()

    def all(self):
        cinema_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]
    
    def update(self, update_to_id, update_first_name, update_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (update_first_name, update_last_name, update_to_id)
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete)
        )
        self._connection.commit()
