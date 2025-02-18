import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)

        )
        self._connection.commit()

    def all(self):
        actors_names = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*actor) for actor in actors_names
        ]

    def update(self, id_to_up, first_name, last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_to_up)
        )
        self._connection.commit()

    def delete(self, id_to_del):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_del,)
        )
        self._connection.commit()
