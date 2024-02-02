import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db")

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )

        return [
            Actor(*row) for row in cinema_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )

        self._connection.commit()

    def update(self,
               actor_id: int,
               new_first_name: str,
               new_last_name: str
               ) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, actor_id,)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
