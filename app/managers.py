import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """
        )
        self.conn.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        query = (
            f"""
            SELECT first_name, last_name, id
            FROM {self.table_name}
            """
        )
        cursor = self.conn.execute(query)
        return [Actor(*row) for row in cursor.fetchall()]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ? WHERE id = ?
            """
        )
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        query = (
            f"""
            DELETE
            FROM {self.table_name}
            WHERE id = ?
            """
        )
        self.conn.execute(query, (pk,))
        self.conn.commit()
