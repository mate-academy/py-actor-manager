import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "Actor "

    def create(self, first_name, last_name):
        self._connection.execute(f"INSERT INTO {self.table_name} "
                                 "(first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name))
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            "SELECT id, first_name, last_name"
            " FROM Actor")
        return [Actor(*row) for row in actor_cursor]

    def update(self, id_to_update, first_name, last_name):
        self._connection.execute(f"UPDATE {self.table_name} "
                                 "SET (first_name, last_name) = (?, ?)"
                                 "WHERE id = ?",
                                 (first_name, last_name, id_to_update))
        self._connection.commit()

    def delete(self, id_to_remove):
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 "WHERE id = ?",
                                 (id_to_remove,))

        self._connection.commit()
