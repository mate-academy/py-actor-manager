import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE actor_id=? ",
            (id,)
        )
        self._connection.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name=?, last_name=? "
            "WHERE actor_id=? ",
            (first_name, last_name, id)
        )
        self._connection.commit()
