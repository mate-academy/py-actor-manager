import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.sqlite_connection = sqlite3.connect(self.db_name)
        self.cursor = self.sqlite_connection.cursor()

        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS "
            f"{self.table_name} ("
            f"id INTEGER PRIMARY KEY, "
            f"first_name TEXT, last_name TEXT)"
        )

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.sqlite_connection.commit()

    def all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return [
            Actor(row[0], row[1], row[2])
            for row in self.cursor.fetchall()
        ]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE ID = ?",
            (new_first_name, new_last_name, pk)
        )

        self.sqlite_connection.commit()

    def delete(
            self,
            pk: int
    ) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE ID = {pk}")
        self.sqlite_connection.commit()
