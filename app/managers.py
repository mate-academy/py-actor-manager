import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            conn.execute(
                f"""
                    CREATE TABLE IF NOT EXISTS {self.table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL
                    )
                    """
            )

    def create(self, first_name: str, last_name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query_add = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """
            c.execute(query_add, (first_name, last_name))

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query_update = f"""
            UPDATE {self.table_name} SET first_name = ?, last_name = ?
            WHERE id = ?
            """
            c.execute(query_update, (new_first_name, new_last_name, pk))

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query_delete = f"""
            DELETE FROM {self.table_name} WHERE id = ?
            """
            c.execute(query_delete, (pk,))

    def all(self) -> list[Actor]:
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query_select = f"""
            SELECT * FROM {self.table_name}
            """
            c.execute(query_select)

            rows = c.fetchall()
            return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]
