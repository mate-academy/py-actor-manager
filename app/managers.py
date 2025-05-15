import sqlite3

from app.models import Actor
from typing import List



# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
                        (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.cursor()
        actors_cursor.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors_cursor]

    def update(self, pk: int,
               new_first_name: str,
               new_last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} "
                       f"WHERE id = ?", (pk,))
        self._connection.commit()