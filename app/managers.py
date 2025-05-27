import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                """,
                (first_name, last_name)
            )
            conn.commit()

    def all(self) -> list[Actor]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute(f"SELECT * FROM {self.table_name}")
            return [Actor(*row) for row in cursor.fetchall()]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (new_first_name, new_last_name, pk)
            )
            conn.commit()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
                """,
                (pk,)
            )
            conn.commit()
