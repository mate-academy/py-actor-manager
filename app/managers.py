import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"
        self.initialize_db()

    def initialize_db(self) -> None:
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name}"
            f" (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f" first_name TEXT NOT NULL, "
            f" last_name TEXT NOT NULL)"
        )
        self._connection.commit()

    def create(self, first_name: str,
               last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        library_format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in library_format_cursor
        ]

    def update(self, id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?,"
            f" last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
