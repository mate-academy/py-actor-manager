import sqlite3
from models import Actor


class ActorManager:
    def __int__(self):
        self._connection = sqlite3.connect(
            "/Users/denis/PycharmProjects/"
            "py-cinema-hall-manager/cinema.db"
        )
        self.table_name = "cinema"

    def create(self, first_name_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name) VALUES (?)",
            (first_name_,)
        )
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, id_to_update: int, fn_update: str, ln_update: str):
        self._connection.execute(
            "UPDATE {self.table_name} "
            "SET first_name = ? AND last_name = ? WHERE id = ?",
            (fn_update, ln_update, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
