import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)"
        )
        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table}"
        cursor = self._connection.execute(query)
        return [Actor(*row) for row in cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        query = (
            f"UPDATE {self.table} SET first_name =?, last_name = ? WHERE id= ?"
        )
        self._connection.execute(query, (id_, first_name, last_name))
        self._connection.commit()

    def delete(self, id_: int) -> None:
        query = f"DELETE FROM {self.table} WHERE id =?"
        self._connection.execute(query, (id_,))
        self._connection.commit()
