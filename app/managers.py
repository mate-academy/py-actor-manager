import sqlite3
from app.models import Actor


class ActorManager():
    def __init__(self, db_name: str, table_name: str) -> None:
        self._db_name = sqlite3.connect(db_name)
        self._table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cur = self._db_name.cursor()
        cur.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._db_name.commit()

    def all(self) -> list[Actor]:
        cur = self._db_name.cursor()
        cur.execute(
            f"SELECT id, first_name, last_name FROM {self._table_name}")
        rows = cur.fetchall()

        actors = []
        for row in rows:
            actors.append(Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]))

        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cur = self._db_name.cursor()
        cur.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._db_name.commit()

    def delete(self, pk: int) -> None:
        cur = self._db_name.cursor()
        cur.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (pk,)
        )
        self._db_name.commit()
