import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect(
            "C:\\sashawork\\py-cinema-hall-manager\\app\\cinema.sqlite"
        )
        self.table_name = "actor"

    def create(self, name, surname):
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (name, surname)
        )
        self.connection.commit()

    def all(self):
        cursor = self.connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*line) for line in cursor]

    def update(self, id_to_update, new_name, new_surname):
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, "
            f"last_name = ?"
            f"WHERE id = ?",
            (new_name, new_surname, id_to_update)

        )
        self.connection.commit()

    def delete(self, id_to_delete):
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete, )
        )
        self.connection.commit()
