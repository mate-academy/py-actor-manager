import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.table = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table}")
        rows = self.cursor.fetchall()
        actors = []
        for row in rows:
            actors.append(Actor(row[0], row[1], row[2]))
        return actors

    def update(
            self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (pk,),
        )
        self.connection.commit()
