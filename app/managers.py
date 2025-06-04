import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self,
                 db_name: str = "actor_manager",
                 table_name: str = "actors") -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(f"{self.db_name}.sqlite")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"pk INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT NOT NULL, "
            f"last_name TEXT NOT NULL)"
        )

        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE pk = ?",
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE pk=?",
            (pk,)
        )
        self.connection.commit()

    def all(self) -> list:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cursor
        ]
