import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._table_name = table_name
        self._conn = sqlite3.connect(db_name)
        self._conn.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> Actor:
        query = (
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cur = self._conn.cursor()
        cur.execute(query, (first_name, last_name))
        self._conn.commit()

        actor_id = cur.lastrowid
        return Actor(
            id=int(actor_id),
            first_name=first_name,
            last_name=last_name,
        )

    def all(self) -> List[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self._table_name}"
        cur = self._conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        if not rows:
            return []

        return [
            Actor(
                id=int(row["id"]),
                first_name=str(row["first_name"]),
                last_name=str(row["last_name"]),
            )
            for row in rows
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        query = (
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        cur = self._conn.cursor()
        cur.execute(query, (new_first_name, new_last_name, pk))
        self._conn.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self._table_name} WHERE id = ?"
        cur = self._conn.cursor()
        cur.execute(query, (pk,))
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def __del__(self) -> None:
        try:
            self._conn.close()
        except Exception:
            pass
