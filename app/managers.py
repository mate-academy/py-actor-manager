import re
import sqlite3

from app.models import Actor

_VALID_TABLE_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        if not _VALID_TABLE_RE.match(table_name):
            raise ValueError("invalid table_name")
        self.db_name = db_name
        self.table_name = table_name
        self.conn: sqlite3.Connection = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self._ensure_table()

    def _ensure_table(self) -> None:
        sql = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL"
            ")"
        )
        self.conn.execute(sql)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        sql = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cur = self.conn.execute(sql, (first_name, last_name))
        self.conn.commit()
        new_id = cur.lastrowid
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        sql = (
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        cur = self.conn.execute(sql)
        rows = cur.fetchall()
        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self.conn.execute(sql, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.conn.execute(sql, (pk,))
        self.conn.commit()

    def __del__(self) -> None:
        try:
            self.conn.close()
        except Exception:
            # evita exceção no coletor de lixo
            pass
