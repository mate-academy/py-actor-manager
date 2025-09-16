import re
import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = self._normalize_table_name(table_name)
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def _normalize_table_name(self, table_name: str) -> str:
        if not re.match(r"^[A-Za-z_]+$", table_name):
            raise ValueError(f"Invalid table name: {table_name}")
        if not table_name.endswith("s"):
            table_name += "s"
        return table_name

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name),
        )
        self.conn.commit()
        pk = self.cursor.lastrowid
        return Actor(pk, first_name, last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [
            Actor(row["id"], row["first_name"], row["last_name"])
            for row in rows
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,),
        )
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()
