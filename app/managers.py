import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self.dbname = "cinema.db"
        self.table_name = "actors"

    def __enter__(self):
        self._connection = sqlite3.connect(self.dbname)
        self._cursor = self._connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._connection.close()

    def create(self, first_name: str, last_name: str):
        self._cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        self._cursor.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in self._cursor]

    def update(self, id_actor: int, first_name: str, last_name: str):
        self._cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id= ?",
            (first_name, last_name, id_actor)
        )

    def delete(self, id_actor: int):
        self._cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {id_actor}"
        )
