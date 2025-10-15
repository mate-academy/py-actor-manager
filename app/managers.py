import sqlite3
import app.models as models

Actor = models.Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        with self.conn:
            self.conn.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                );
                """
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self.conn:
            self.conn.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) "
                f"VALUES (?, ?)",
                (first_name, last_name),
            )

    def all(self) -> list[Actor]:
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        rows = cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self.conn:
            self.conn.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? WHERE id = ?",
                (new_first_name, new_last_name, pk),
            )

    def delete(self, pk: int) -> None:
        with self.conn:
            self.conn.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (pk,),
            )

    def __del__(self) -> None:
        self.conn.close()
