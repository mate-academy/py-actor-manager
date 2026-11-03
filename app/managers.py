import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.table_name = table_name

        with self.connection:
            self.connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self.connection:
            self.connection.execute(
                f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                """,
                (first_name, last_name),
            )

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            f"""
            SELECT id, first_name, last_name
            FROM {self.table_name}
            ORDER BY id
            """
        )

        return [Actor(*row) for row in cursor.fetchall()]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        with self.connection:
            self.connection.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (new_first_name, new_last_name, pk),
            )

    def delete(self, pk: int) -> None:
        with self.connection:
            self.connection.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (pk,),
            )
