import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:
        actors = [
            Actor(*actor)
            for actor in self._connection.execute(
                "SELECT * FROM actors"
            )
        ]
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM actors WHERE id = {pk}",
        )
