import sqlite3

from app.models import Actor
from typing import Any


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)

    def all(self) -> Any:
        db_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(id=db_row[0], first_name=db_row[1], last_name=db_row[2])
            for db_row in db_cursor
        ]

    def delete(self, pk: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )

        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),

        )

        self.conn.commit()

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.conn.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk)
        )

        self.conn.commit()
