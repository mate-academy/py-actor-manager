import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connect = sqlite3.connect("cinema.db3")

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connect.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
        self,
        id_to_update: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:

        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET (first_name, last_name) = (?, ?) "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )

        self._connect.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connect.commit()
