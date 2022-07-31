import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def create(self, first_name_, last_name_):
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            "SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            first_name_to_update: str,
            last_name_to_update: str
    ):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?,"
            "last_name = ?"
            "WHERE id = ?",
            (first_name_to_update, last_name_to_update, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
