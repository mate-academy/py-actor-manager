import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name}"
            f" (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)")

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            actor = Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            result.append(actor)
        return result

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.connection.execute(f"UPDATE {self.table_name}"
                                f" SET first_name = ?, last_name = ?"
                                f" WHERE id = ?",
                                (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.connection.execute(f"DELETE FROM {self.table_name}"
                                f" WHERE id = ?", (pk,))
        self.connection.commit()
