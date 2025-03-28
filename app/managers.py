import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            r"C:\Users\PROBEL\PycharmProjects\py-actor-manager\cinema.sqlite"
        )
        self.actors_table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.actors_table}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.actors_table}"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.actors_table} "
            f"SET first_name = ?, last_name = ? "
            F"WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.actors_table} WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
