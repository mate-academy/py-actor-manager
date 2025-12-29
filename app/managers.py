import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        sql = (
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)"
        )
        self.connection.execute(sql, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        sql = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.execute(sql)
        rows = cursor.fetchall()

        actors = []
        for row in rows:
            actor = Actor(*row)
            actors.append(actor)

        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self.connection.execute(sql, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(sql, (pk,))
        self.connection.commit()