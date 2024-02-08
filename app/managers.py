import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name)"
            " VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [Actor(*params) for params in actors_cursor]

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name}"
            " WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()

    def update(
            self,
            actor_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name}"
            " SET first_name = ?, last_name = ?"
            " WHERE id = ?",
            (actor_id, new_first_name, new_last_name)
        )
        self._connection.commit()
