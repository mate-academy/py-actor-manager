import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def all(self):
        data = self.connection.execute(
            "SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in data]

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self.connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete):
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = (?)",
            (id_to_delete,)
        )
        self.connection.commit()
