import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list:
        result_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in result_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} SET first_name=?,"
            f" last_name=? WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk, )
        )
        self.conn.commit()
