import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            (
                f"INSERT INTO {self.table_name} "
                "(first_name, last_name) VALUES (?, ?)"
            ),
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()

        return [
            Actor(row[0], row[1], row[2])
            for row in rows
        ]

    def update(
        self,
        pk: str,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        self.cursor.execute(
            (
                f"UPDATE {self.table_name} "
                "SET first_name = ?, last_name = ? "
                "WHERE id = ?"
            ),
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: str) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,),
        )
        self.connection.commit()
