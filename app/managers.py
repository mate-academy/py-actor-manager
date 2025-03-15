import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

# C
    def create(self, id: str, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(id, first_name, last_name) "
            "VALUES (?, ?, ?)",
            (id, first_name, last_name,),
        )
        self._connection.commit()

# R
    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

# U
    def update(self,
               id_update: int,
               first_name_update: str,
               last_name_update: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name_update, last_name_update, id_update)
        )
        self._connection.commit()

# D
    def delete(self, id_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
