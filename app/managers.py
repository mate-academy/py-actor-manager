import sqlite3

from app.models import Actor
from typing import List


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT
        )
        """
        self.cursor.execute(sql)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> int:
        sql = (f"INSERT INTO {self.table_name}"
               f" (first_name, last_name) VALUES (?, ?)")
        self.cursor.execute(sql, (first_name, last_name))
        self.connection.commit()
        return self.cursor.lastrowid

    def all(self) -> List[Actor]:
        sql = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        actor_list = [Actor(id=row[0], first_name=row[1],
                            last_name=row[2]) for row in results]
        return actor_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql = (f"UPDATE {self.table_name} "
               f"SET first_name = ?, last_name = ? WHERE id = ?")
        self.cursor.execute(sql, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(sql, (pk,))
        self.connection.commit()
