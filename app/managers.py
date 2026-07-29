import sqlite3

from app.models import Actor


class ActorManager:
    """Manage actors in the database."""

    def __init__(
            self,
            db_name: str,
            table_name: str = "actors") -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def create(
            self,
            first_name: str,
            last_name: str,
    ) -> Actor:
        """Create a new actor in the database."""
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) "
                "VALUES (?, ?)",
                (first_name, last_name)
            )
            conn.commit()
            actor_id = cursor.lastrowid
        return Actor(
            id=actor_id,
            first_name=first_name,
            last_name=last_name
        )

    def all(self) -> list[Actor]:
        """Retrieve all actors from the database."""
        if not self.table_name:
            return []

        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT id, first_name, last_name FROM {self.table_name}"
            )
            rows = cursor.fetchall()
        return [Actor(
            id=row[0],
            first_name=row[1],
            last_name=row[2]) for row in rows]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> Actor:
        """Update an existing actor in the database."""
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self.table_name} "
                "SET first_name = ?, last_name = ? "
                "WHERE id = ?",
                (new_first_name, new_last_name, pk)
            )
            conn.commit()
        return Actor(
            id=pk,
            first_name=new_first_name,
            last_name=new_last_name
        )

    def delete(self, pk: int) -> None:
        """Delete an actor from the database."""
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?", (pk,)
            )
            conn.commit()
