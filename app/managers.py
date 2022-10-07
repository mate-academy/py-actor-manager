import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connect = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connect.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connect.commit()

    def all(self):
        cinema_actors_cursor = self._connect.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in cinema_actors_cursor]

    def update(self, new_first_name, new_last_name, id_of_actor_to_change):
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, id_of_actor_to_change)
        )
        self._connect.commit()

    def delete(self, id_actor_to_delete):
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_actor_to_delete,)
        )
        self._connect.commit()
