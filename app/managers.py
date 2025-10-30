import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    # Create - C
    def create(
        self,
        first_name: str,
        last_name: str,
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f" VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    # RETRIEVE - R
    def all(self) -> List[Actor]:
        literary_format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in literary_format_cursor]

    # UPDATE - U
    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ? , last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, pk),
        )
        self._connection.commit()

    # DELETE - D
    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} " "WHERE id = ? ", (pk,)
        )
        self._connection.commit()
