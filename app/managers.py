import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                "id INTEGER PRIMARY KEY, "
                "first_name VARCHAR(50) NOT NULL, "
                "last_name VARCHAR(50) NOT NULL"
                ")"
            )

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
