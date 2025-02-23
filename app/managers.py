import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "cinema"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            " VALUES (?, ?)"
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in cursor]

    def update(self,
               id_to_update: int,
               first_name: str,
               last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name = ?"
            " WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self.connection.commit()

    def delete(self,
               id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
