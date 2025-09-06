import sqlite3
from typing import List, Optional
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        cursor = self.conn.execute(query, (first_name, last_name))
        self.conn.commit()
        return Actor(
            id=cursor.lastrowid,
            first_name=first_name,
            last_name=last_name
        )

    def all(self) -> List[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        return [
            Actor(id=row["id"], first_name=row["first_name"],
                  last_name=row["last_name"]) for row in rows
        ]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> Optional[Actor]:
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? "
                 f"WHERE id = ?")
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()
        return self.get(pk)

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.conn.execute(query, (pk,))
        self.conn.commit()

    def get(self, pk: int) -> Optional[Actor]:
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        cursor = self.conn.execute(query, (pk,))
        row = cursor.fetchone()
        if row:
            return Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"])
        return None
