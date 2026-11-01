import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        # Table names cannot be passed as SQL parameters, so quote the name as
        # an SQLite identifier and escape any embedded quotes.
        self.table_name = table_name
        self._quoted_table_name = '"' + table_name.replace('"', '""') + '"'

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._quoted_table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self._quoted_table_name}"
        )
        return [Actor(*row) for row in cursor.fetchall()]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self._quoted_table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._quoted_table_name} WHERE id = ?",
            (pk,),
        )
        self._connection.commit()
