import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db3")
        self.table_name = "actor"

    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self):
        actors_cursor = self.connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update: int,
               new_first_name: str,
               new_last_name: str):
        self.connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int):
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
