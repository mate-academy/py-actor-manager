import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        actor = Actor(first_name=first_name, last_name=last_name)
        self._conn.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (actor.first_name, actor.last_name)
        )
        self._conn.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute("SELECT * FROM actor")
        return [Actor(*row) for row in self._cursor]

    def update(self, pk: str, new_first_name: str, new_last_name: str) -> None:
        self._conn.execute(
            "UPDATE actor SET first_name=?, last_name=? WHERE pk=?",
            (new_first_name, new_last_name, pk)
        )
        self._conn.commit()

    def delete(self, pk: str) -> None:
        self._conn.execute(
            "DELETE FROM actor WHERE pk=?",
            (pk)
        )
        self._conn.commit()
