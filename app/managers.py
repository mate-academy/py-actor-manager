import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str = "actors") -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL)"
        )
        self.connection.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name))
        self.connection.commit()
        actor_id = cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        query = (f"UPDATE {self.table_name} SET first_name=?, "
                 f"last_name=? WHERE id=?")
        cursor = self.connection.cursor()
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete(self, pk: int) -> bool:
        query = f"DELETE FROM {self.table_name} WHERE id=?"
        cursor = self.connection.cursor()
        cursor.execute(query, (pk,))
        self.connection.commit()
        return cursor.rowcount > 0

    def __del__(self) -> None:
        self.connection.close()
