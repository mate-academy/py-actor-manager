import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = self.db_name.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.db_name.commit()

    def all(self) -> List[Actor]:
        actors = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actors
        ]

    def update(
            self,
            actor_id: int,
            actor_first_name: str,
            actor_last_name: str
    ) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (actor_first_name, actor_last_name, actor_id)
        )

        self.db_name.commit()

    def delete(self, actor_id: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (actor_id,)
        )

        self.db_name.commit()
