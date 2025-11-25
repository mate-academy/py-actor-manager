import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        create_query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL"
            ")"
        )
        self.cursor.execute(create_query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        insert_query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        self.cursor.execute(insert_query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> List[Actor]:
        select_query = (
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        rows = self.cursor.execute(select_query).fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        update_query = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self.cursor.execute(update_query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        delete_query = (
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?"
        )
        self.cursor.execute(delete_query, (pk,))
        self.conn.commit()
