import sqlite3
from app.models import Actor


class ActorManager:
    TABLE_NAME = "actors"

    def __init__(self, db_name: str, table_name: str | None = None) -> None:
        self.db_name = db_name
        self._connection = sqlite3.connect(self.db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL)"
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self._connection.execute(
            f"INSERT INTO {self.TABLE_NAME}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()
        actor_id = cursor.lastrowid
        return Actor(actor_id, first_name, last_name)

    def all(self) -> list[Actor]:
        execute = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.TABLE_NAME}"
        )
        return [Actor(*row) for row in execute]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        cursor = self._connection.execute(
            f"UPDATE {self.TABLE_NAME}"
            f" SET first_name=?, last_name=? WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, pk: int) -> bool:
        cursor = self._connection.execute(
            f"DELETE FROM {self.TABLE_NAME} WHERE id=?",
            (pk,)
        )
        self._connection.commit()
        return cursor.rowcount > 0

    def __del__(self) -> None:
        self._connection.close()
