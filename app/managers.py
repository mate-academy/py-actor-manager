import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_actors = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_actors} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        all_actors = self._connection.execute(
            f"SELECT * FROM {self.table_actors}"
        )
        return [Actor(*actor) for actor in all_actors]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_actors} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_actors} WHERE id = ?",
            (id,)
        )
        self._connection.commit()
