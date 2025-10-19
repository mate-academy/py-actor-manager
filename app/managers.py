import sqlite3
import re

from app.models import Actor
from typing import Optional, Type, Any


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self._validate_table_name(table_name)
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def _validate_table_name(self, name: str) -> None:
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
            raise ValueError(f"Invalid table name: {name}")

    def create(self, first_name: str, last_name: str) -> int:
        query = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
        """
        cursor = self.conn.execute(query, (first_name, last_name))
        self.conn.commit()
        return cursor.lastrowid

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()

        return [Actor(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"]
        ) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        query = f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """
        cursor = self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()
        return cursor.rowcount > 0

    def delete(self, pk: int) -> bool:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        cursor = self.conn.execute(query, (pk,))
        self.conn.commit()
        return cursor.rowcount > 0

    def close(self) -> None:
        if self.conn:
            self.conn.close()

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Any]
    ) -> None:
        self.close()
