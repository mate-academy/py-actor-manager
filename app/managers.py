import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?,?)",
            (first_name, last_name))
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def delete(self, id_to_del):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_del,)
        )
        self._connection.commit()

    def update(self, id_to_update, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?", (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()
