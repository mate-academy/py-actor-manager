import sqlite3
from sqlite3 import Cursor
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = self.conn.cursor()
        table_exist = self._table_exist(query, self.table_name)
        if not table_exist:
            # Create table if no exist
            query.execute(
                f"""
                CREATE TABLE {self.table_name} (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(100),
                last_name VARCHAR(100))
                """
            )
        query.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list:
        query = self.conn.cursor()
        table_exist = self._table_exist(query, self.table_name)
        if not table_exist:
            return []
        # Return list of Actor class from table
        actors = query.execute(
            f"""
            SELECT * FROM {self.table_name}
            """
        ).fetchall()
        return [Actor(actor[0], actor[1], actor[2]) for actor in actors]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = self.conn.cursor()
        table_exist = self._table_exist(query, self.table_name)
        if table_exist:
            record_exist = self._record_exist(query, self.table_name, pk)
            if record_exist:
                # Update record
                query.execute(
                    f"""
                    UPDATE {self.table_name}
                    SET first_name = ?, last_name = ?
                    WHERE id = ?
                    """,
                    (new_first_name, new_last_name, pk)
                )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        query = self.conn.cursor()
        table_exist = self._table_exist(query, self.table_name)
        if table_exist:
            record_exist = self._record_exist(query, self.table_name, pk)
            if record_exist:
                # Delete record
                query.execute(
                    f"""
                    DELETE FROM {self.table_name}
                    WHERE id = ?
                    """,
                    (pk, )
                )
        self.conn.commit()

    @staticmethod
    def _table_exist(query: Cursor, table_name: str) -> bool:
        # Check if table exists
        table_exist = query.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            AND name = ?
            """,
            (table_name, )
        ).fetchone()
        if table_exist is None:
            return False
        return True

    @staticmethod
    def _record_exist(query: Cursor, table_name: str, pk: int) -> bool:
        # Check if record exists
        record_exist = query.execute(
            f"""
            SELECT * FROM {table_name}
            WHERE id = ?
            """,
            (pk, )
        ).fetchone()
        if not record_exist:
            return False
        return True
