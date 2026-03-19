import sqlite3

from app.models import Actor


class ActorManager():
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.c = self.connection.cursor()
        self.c.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"id INTEGER PRIMARY KEY, "
            f"first_name TEXT, "
            f"last_name TEXT"
            f")"
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.c.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.c.execute(f"SELECT * FROM {self.table_name}")
        return [
            Actor(id=actor[0], first_name=actor[1], last_name=actor[2])
            for actor in self.c
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.c.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.c.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()
