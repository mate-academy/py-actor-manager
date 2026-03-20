import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conn.commit()

    def all(self) -> list[Actor]:
        cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        actor_list = [
            Actor(*row) for row in cursor
        ]
        if actor_list:
            return actor_list
        else:
            return []

    def update(self, pk: int, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"UPDATE {self.table_name} SET first_name = ?, "
            "last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, pk)
        )
        self._conn.commit()

    def delete(self, pk: int) -> None:
        self._conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self._conn.commit()
