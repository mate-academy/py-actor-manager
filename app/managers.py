# flake8: noqa
import sqlite3 as sq
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sq.connect(
            "/Users/antonbliznuk/Education/MateAcademy/GitHubTasks/py-actor-manager/cinema.sqlite3"
        )
        self.table_name = "actors"

    def all(self) -> list:
        result = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        ).fetchall()
        return [
            Actor(actor[0], actor[1], actor[2]) for actor in result
        ]

    def create(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (id, first_name, last_name) "
            "VALUES (?, ?, ?)",
            (id_, first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
