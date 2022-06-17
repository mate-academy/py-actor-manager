import sqlite3

from modules import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actor"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        cursor = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in cursor]

    def update(self, id, first_name, last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id,)
        )
        self._connection.commit()
