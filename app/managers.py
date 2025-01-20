import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()


    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor() for row in actors_cursor
        ]

    def update(self, id: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self.table} SET first_name = ?, last_name = ? WHERE id = ?",
            (id, first_name, last_name)
        )
        self._connection.commit()

    def delete(self, id):
        self._connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (id,)
        )
        self._connection.commit()
