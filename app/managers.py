import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def all(self) -> list:
        actors_data_cursor = self._connection.execute(
            f"SELECT id, first_name, "
            f"last_name FROM {self.table_name}")
        return [Actor(*row) for row in actors_data_cursor]

    def create(self,
               first_name: str,
               last_name: str) -> None:

        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) values (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, actor_id: int,
               new_name: str,
               new_last_name: str) -> None:

        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, "
            "last_name = ? WHERE id = ?",
            (new_name, new_last_name, actor_id))

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
