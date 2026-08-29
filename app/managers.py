import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.actor_id = 0
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        actor = Actor(id=self.actor_id + 1, first_name=first_name, last_name=last_name)
        self._conn.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (actor.first_name, actor.last_name)
        )
        self._conn.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute(f"SELECT * FROM {self.table_name}")
        if self._cursor.rowcount == 0:
            return []
        return [Actor(*row) for row in self._cursor]

    def update(self, pk: str, new_first_name: str, new_last_name: str) -> None:
        self._conn.execute(
            f"UPDATE {self.table_name} "
            "SET first_name=?, last_name=? WHERE pk=?",
            (new_first_name, new_last_name, pk)
        )
        self._conn.commit()

    def delete(self, pk: str) -> None:
        self._conn.execute(
            f"DELETE FROM {self.table_name} WHERE pk=?",
            (pk)
        )
        self._conn.commit()
