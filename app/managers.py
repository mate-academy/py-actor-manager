import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        if (
            not isinstance(table_name, str)
            or not table_name
            or "\x00" in table_name
        ):
            raise ValueError(
                "table_name must be a non-empty string without null bytes"
            )

        # Quote the table identifier safely.
        self.table_name = '"' + table_name.replace('"', '""') + '"'
        self.connection = sqlite3.connect(db_name)

        with self.connection:
            self.connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "first_name TEXT NOT NULL, "
                "last_name TEXT NOT NULL)"
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self.connection:
            self.connection.execute(
                f"INSERT INTO {self.table_name} "
                "(first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )

    def all(self) -> list[Actor]:
        rows = self.connection.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name} ORDER BY id"
        ).fetchall()

        return [Actor(*row) for row in rows]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        with self.connection:
            self.connection.execute(
                f"UPDATE {self.table_name} "
                "SET first_name = ?, last_name = ? WHERE id = ?",
                (new_first_name, new_last_name, pk),
            )

    def delete(self, pk: int) -> None:
        with self.connection:
            self.connection.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (pk,),
            )
