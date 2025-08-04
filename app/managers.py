import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL"
            ")"
        )
        self.cursor.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

        # Get the ID of the newly created actor
        actor_id = self.cursor.lastrowid
        if actor_id is None:
            raise RuntimeError("Failed to get ID of newly created actor")
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2])
                for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (pk,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
