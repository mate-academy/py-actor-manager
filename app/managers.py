import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connector = sqlite3.connect(db_name)
        self.table = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self.connector.execute(
            f"INSERT INTO {self.table} (first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name)
        )
        self.connector.commit()

    def all(self) -> list[Actor]:
        cursor = self.connector.execute(
            f"SELECT * FROM {self.table}"
        )
        return list([Actor(*row) for row in cursor])

    def update(self, pk: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.connector.execute(
            f"UPDATE {self.table} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connector.commit()

    def delete(self, pk: int) -> None:
        self.connector.execute(
            f"DELETE FROM {self.table} "
            "WHERE id = ?",
            (pk,)
        )
        self.connector.commit()
