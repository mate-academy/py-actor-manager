import sqlite3
from typing import List, Tuple


try:
    from .models import Actor
except ImportError:
    from models import Actor


class ActorManager:
    # Dodano -> None dla metody specjalnej (ANN204)
    def __init__(self, db_name: str = "cinema.db",
                 table_name: str = "actors") -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._create_table()

    # Dodano -> sqlite3.Connection dla metody chronionej (ANN202)
    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_name)

    def _create_table(self) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
            """)
            conn.commit()

    def create(self, first_name: str, last_name: str) -> int:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self.table_name} "
                f"(first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )
            conn.commit()
            return cursor.lastrowid

    def _map_row_to_actor(self, row: Tuple) -> Actor:
        return Actor(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
        )

    def all(self) -> List[Actor]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = cursor.fetchall()
            return [self._map_row_to_actor(row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self.table_name} SET "
                f"first_name=?, last_name=? WHERE id=?",
                (new_first_name, new_last_name, pk)
            )
            conn.commit()

    def delete(self, pk: int) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (pk,))
            conn.commit()
