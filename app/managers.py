from dataclasses import dataclass
import sqlite3

from models import Actor


@dataclass
class ActorManager:
    _connection = sqlite3.connect("cinema.db3")
    table_name = "actors"

    def all(self) -> list[Actor]:
        cinema_cursor = self._connection.execute(
            "SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cinema_cursor]

    def create(self,
               first_name: str,
               last_name: str
               ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self,
               id_to_update: int,
               new_first_name: str,
               new_last_name: str
               ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, "
            f"last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
