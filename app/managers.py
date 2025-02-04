import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in cursor]

    def update(
            self,
            id_to_update: int,
            first_name: str = None,
            last_name: str = None
    ) -> None:
        to_update = []
        values = []

        if first_name is not None:
            to_update.append("first_name = ?")
            values.append(first_name)

        if last_name is not None:
            to_update.append("last_name = ?")
            values.append(last_name)

        self._connection.execute(
            f"UPDATE actors SET {', '.join(to_update)} WHERE id = ?",
            (*values, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
