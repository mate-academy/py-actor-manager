import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self):
        actors_data = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_data]

    def create(self, first_name, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET (first_name, last_name) = (?, ?) "
            f"WHERE id  = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
