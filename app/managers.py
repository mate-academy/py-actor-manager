import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(
            self,
            first_name: str,
            last_name: str,
    ) -> None:
        self._connection.execute(
            f"INSERT INTO  {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_connection_cursor = self._connection.execute(
            f"SELECT * FROM  {self.table_name}"
        )
        return [
            Actor(*actor)
            for actor in actor_connection_cursor
        ]

    def update(
            self,
            id: int,
            first_name_update: str,
            last_name_update: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (
                first_name_update,
                last_name_update,
                id
            )
        )
        self._connection.commit()

    def delete(
            self,
            id: int
    ) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id,)
        )
        self._connection.commit()
