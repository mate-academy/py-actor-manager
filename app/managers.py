import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self.connect.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self.connect.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self.connect.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in actor_cursor
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        self.connect.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        self.connect.commit()

    def delete(self, pk: int) -> None:
        self.connect.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,),
        )
        self.connect.commit()
