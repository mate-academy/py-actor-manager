import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.execute("SELECT * FROM actors")
        return [
            Actor(*actor) for actor in cursor
        ]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} SET "
            f"first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id,)
        )
        self.connection.commit()
