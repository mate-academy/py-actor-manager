import sqlite3

from app.models import Actor

from typing import List


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        sql = (f"INSERT INTO {self.table_name} "
               f"(first_name, last_name) VALUES (?, ?)")
        self.cursor.execute(sql, (first_name, last_name))
        self.conn.commit()

    def all(self) -> List[Actor]:
        list_of_actors = []
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        all = self.cursor.fetchall()
        for row in all:
            list_of_actors.append(Actor(*row))
        return list_of_actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql = (f"UPDATE {self.table_name} "
               f"SET first_name = ?, "
               f"last_name = ? "
               f"WHERE id = ?")
        self.cursor.execute(sql, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(sql, (pk,))
        self.conn.commit()
