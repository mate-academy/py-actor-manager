import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name_of: str, last_name_of: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name_of, last_name_of)
        )
        self._connection.commit()

    def delete(self, id: str) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id,)
        )
        self._connection.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id =?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]
