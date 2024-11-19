import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("../cinema.sqlite")
        self._table_name = "actor"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self._table_name}"
            f"(first_name, last_name) VALUES (?,  ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self._table_name};"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, which_id_to_update: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (first_name, last_name, which_id_to_update)
        )
        self._connection.commit()

    def delete(self, which_id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (which_id_to_delete,)
        )
        self._connection.commit()
