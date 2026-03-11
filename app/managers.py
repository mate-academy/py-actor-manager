import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(f"{self.db_name}")

    def all(self) -> list[Actor]:
        actor_cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        actors = []
        for actor in actor_cursor:
            actors.append(Actor(actor))

        return actors
