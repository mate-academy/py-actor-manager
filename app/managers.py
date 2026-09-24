import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)"
        )
        with self.connection:
            self.connection.execute(query, (first_name, last_name))

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.execute(query)
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor.fetchall()
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?"
        )
        with self.connection:
            self.connection.execute(
                query, (new_first_name, new_last_name, pk)
            )

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with self.connection:
            self.connection.execute(query, (pk,))
