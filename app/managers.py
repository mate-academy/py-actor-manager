import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name }"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        db_name_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in db_name_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE  id = ? ",
            (pk,)
        )
        self.connection.commit()
