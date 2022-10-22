import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update, first_name, last_name):
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
