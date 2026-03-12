import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(f"{self.db_name}")

    def create(self, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?)",
            (first_name, last_name)
        )
        self._conn.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actor_cursor
        ]

