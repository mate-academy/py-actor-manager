from app.models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            "D:/python_db/py-actor-manager/cinema.sqlite"
        )
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [
            Actor(*row) for row in actors
        ]

    def update(
            self,
            id_to_change: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (first_name, last_name, id_to_change)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (id_to_delete, )
        )
        self._connection.commit()

    def __del__(self) -> None:
        self._connection.close()
