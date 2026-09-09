import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        with self.conn:
            self.conn.execute(
                f"""
                    CREATE TABLE IF NOT EXISTS {self.table_name} (\
                    id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    first_name TEXT NOT NULL, \
                    last_name TEXT NOT NULL)"""
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self.conn:
            query_add = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """
            self.conn.execute(query_add, (first_name, last_name))

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self.conn:
            query_update = f"""
            UPDATE {self.table_name} SET first_name = ?, last_name = ?
            WHERE id = ?
            """
            self.conn.execute(
                query_update,
                (new_first_name, new_last_name, pk))

    def delete(self, pk: int) -> None:
        with self.conn:
            query_delete = f"""
            DELETE FROM {self.table_name} WHERE id = ?
            """
            self.conn.execute(query_delete, (pk,))

    def all(self) -> list[Actor]:
        with self.conn:
            query_select = f"""
            SELECT * FROM {self.table_name}
            """

            cursor = self.conn.cursor()
            cursor.execute(query_select)

            return [Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2])
                for row in cursor.fetchall()]
