import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self) -> None:
        """Create table if it does not exist."""
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            + "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            + "first_name TEXT NOT NULL, last_name TEXT NOT NULL)")
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        """Create a new actor record."""
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        """Return all actors from database."""
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """Update actor by primary key."""
        self.connection.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        """Delete actor by primary key."""
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,),
        )
        self.connection.commit()
