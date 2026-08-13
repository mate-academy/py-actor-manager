import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        connection = sqlite3.connect(self.db_name)

        connection.execute(
            f"INSERT "
            f"INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        connection.commit()

    def all(self) -> list[Actor]:
        connection = sqlite3.connect(self.db_name)
        return [
            Actor(*row) for row in connection.execute(
                f"SELECT * FROM {self.table_name}"
            )
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        connection = sqlite3.connect(self.db_name)
        connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        connection.commit()

    def delete(self, pk: int) -> None:
        connection = sqlite3.connect(self.db_name)
        connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,),
        )
        connection.commit()
