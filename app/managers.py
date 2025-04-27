import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.sqlite")
        self.table_name = "actors"

    # CRUD
    # - CREATE
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connection.commit()

    # READ
    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(
                first_name=first_name,
                last_name=last_name,
                id=id_
            )
            for first_name, last_name, id_ in cursor
        ]

    # UPDATE
    def update(
            self, id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id_,)
        )

        self._connection.commit()
