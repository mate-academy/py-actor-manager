import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../actors_db.sqlite")
        self.table = "actors"

    def all(self) -> list[Actor]:
        router = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row) for row in router
        ]

    def update(self,
               actor_id: int,
               first_name: str,
               new_last_name: str
               ) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, new_last_name, actor_id)
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (FIRST_NAME, LAST_NAME) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
