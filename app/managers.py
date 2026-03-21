import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT
            )
            """  # noqa: E231, E241, E202
        )
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        query = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
        """
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        query = f"""
            SELECT id, first_name, last_name
            FROM {self.table_name}
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return [Actor(*row) for row in rows]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        query = f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """
        self.cursor.execute(
            query,
            (new_first_name, new_last_name, pk),
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("Actor not found")

    def delete(self, pk: int) -> None:
        query = f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
        """
        self.cursor.execute(query, (pk,))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
