import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name} "
                            f"(first_name, last_name) VALUES (?, ?)",
                            (first_name, last_name))
        self.conn.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        actors = [Actor(id=row[0], first_name=row[1],
                        last_name=row[2]) for row in rows]
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(f"UPDATE {self.table_name} "
                            f"SET first_name = ?, last_name = ? WHERE id = ?",
                            (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                            (pk,))
        self.conn.commit()
