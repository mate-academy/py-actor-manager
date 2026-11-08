import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)"
        )
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (pk,))
        self.conn.commit()

    def __del__(self) -> None:
        if hasattr(self, "conn"):
            self.conn.close()
