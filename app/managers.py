import sqlite3

from typing import Any

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.table_name = table_name
        self.conn.row_factory = sqlite3.Row

    def _row_to_actor(self, row: dict) -> Any:
        return Actor(id=row["id"],
                     first_name=row["first_name"],
                     last_name=row["last_name"])

    def create(self, first_name: str, last_name: str) -> Any:
        with self.conn:
            cur = self.conn.execute(
                f"INSERT INTO {self.table_name}"
                "(first_name, last_name) VALUES(?,?)",
                (first_name, last_name,))

            new_id = cur.lastrowid
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    def all(self) -> list:
        with self.conn:
            cur = self.conn.execute(
                f"SELECT id, first_name, last_name FROM {self.table_name}")

            rows = cur.fetchall()
        return [self._row_to_actor(r) for r in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> Any:
        with self.conn:
            updt_row = self.conn.execute(f"UPDATE {self.table_name}"
                                         " SET first_name = ?,"
                                         " last_name = ? WHERE id =?",
                                         (new_first_name, new_last_name, pk,))
            if updt_row.rowcount == 0:
                return None
            else:
                cur = self.conn.execute(f"SELECT * FROM {self.table_name}"
                                        " WHERE id = ?", (pk,))
                row = cur.fetchone()
        return self._row_to_actor(row)

    def delete(self, pk: int) -> bool:
        with self.conn:
            cur = self.conn.execute(f"DELETE FROM {self.table_name}"
                                    " WHERE id = ?", (pk,))
            return bool(cur.rowcount)
