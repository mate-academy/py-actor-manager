import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor] | None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
