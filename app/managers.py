import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._conection = sqlite3.connect(db_name)
        self.table = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._conection.execute(
            f"INSERT INTO {self.table} (FIRST_NAME, LAST_NAME) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conection.commit()

    def all(self) -> list[Actor]:
        cursor = self._conection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row)
            for row in cursor
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        self._conection.execute(
            f"UPDATE {self.table} "
            "SET FIRST_NAME = ?, LAST_NAME = ? "
            "WHERE ID = ?",
            (new_first_name, new_last_name, pk)
        )
        self._conection.commit()

    def delete(self, pk: int) -> None:
        self._conection.execute(
            f"DELETE FROM {self.table} WHERE ID = ?",
            (pk, )
        )
