import sqlite3

from app.models import Actor


class ActorManager:
    """Manager that provides CRUD operations for ``Actor`` model."""

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        """Create a new actor record in the database."""

        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        )
        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        """Return a list of ``Actor`` instances from the database."""

        query = (
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        cursor = self.connection.execute(query)
        rows = cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """Update actor record with provided ``pk``."""

        query = (
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self.connection.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        """Delete actor record with provided ``pk`` from the database."""

        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(query, (pk,))
        self.connection.commit()

