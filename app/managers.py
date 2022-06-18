import sqlite3

from models import Actor


class ActorManager:

    def __init__(self):
        self.connection = sqlite3.connect("cinema_db.db3")
        self.name_of_db = "actors"

    def all(self):

        cinema_data_cursor = self.connection.execute(
            f"SELECT id, first_name, last_name FROM {self.name_of_db}"
        )

        return [Actor(*row) for row in cinema_data_cursor]

    def create(self, first_name: str, last_name: str):

        self.connection.execute(
            f"INSERT INTO {self.name_of_db} (first_name, last_name)"
            " VALUES (?, ?)", (first_name, last_name)
        )
        self.connection.commit()

    def update(self, id_to_update: int, first_name_: str, last_name_: str):

        self.connection.execute(
            f"UPDATE {self.name_of_db} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name_, last_name_, id_to_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int):

        self.connection.execute(
            f"DELETE FROM {self.name_of_db}"
            " WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
