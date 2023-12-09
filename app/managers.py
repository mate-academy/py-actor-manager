import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO "
            f"{self.table_name} (first_name, last_name)"
            f" VALUES(?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id_to_update: int,
               first_name: str,
               last_name: str
               ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name = ?"
            " WHERE id = ?",
            (first_name, last_name, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_del: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name}"
            " WHERE id = ?",
            (id_to_del,)
        )
        self._connection.commit()
