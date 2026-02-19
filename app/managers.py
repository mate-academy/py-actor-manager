import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connect = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connect.execute(
            f"SELECT * FROM {self.table_name}",
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connect.commit()

    def delete(self, pk: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self._connect.commit()
