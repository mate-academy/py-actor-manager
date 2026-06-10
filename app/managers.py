import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()
        self.table_name = table_name

    def _execute(self, comand: str, params: tuple = ()) -> sqlite3.Cursor:
        self._cursor.execute(comand, params)
        self._connection.commit()
        return self._cursor

    def create(self, first_name: str, last_name: str) -> None:
        self._execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )

    def all(self) -> list:
        rows = self._execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )

    def delete(self, pk: int) -> None:
        self._execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))


# if __name__ == "__main__":
#     manager = ActorManager("cinema.sqlite", "actors")
#     manager._execute("""
#         CREATE TABLE IF NOT EXISTS actors (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL
#         )
#     """)
#     # manager.create("Gena", "Zubarev")
#     print(manager.all())
