import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )

    def all(self) -> None:
        cinema_actors_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cinema_actors_cursor]

    def update(self,
               id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} SET first_name = ? , last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
