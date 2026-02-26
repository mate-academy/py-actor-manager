import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT, "
            "last_name TEXT)"
        )

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 "(first_name, last_name) VALUES (?, ?)")
        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self._connection.execute(query, (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._connection.execute(query, (pk,))
        self._connection.commit()
