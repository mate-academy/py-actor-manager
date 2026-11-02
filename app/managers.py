import sqlite3

from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)
        self._connection.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )""",
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self._connection.cursor()
        cursor.execute(
            f"""INSERT INTO {self.table_name}
                (first_name, last_name)
                VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self._connection.commit()
        return Actor(id=cursor.lastrowid, first_name=first_name,
                     last_name=last_name)

    def all(self) -> List[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT id, first_name, last_name "
                       f"FROM {self.table_name}")
        rows = cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1],
                      last_name=row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"""UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?""",
            (new_first_name, new_last_name, pk),
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"""DELETE FROM {self.table_name}
                WHERE id = ?""",
            (pk,),
        )
        self._connection.commit()
