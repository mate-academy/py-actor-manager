import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()
        self.table_name = table_name
        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT NOT NULL, "
            f"last_name TEXT NOT NULL)"
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        all_actors = self._cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in all_actors]

    def update(
            self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        self._cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
