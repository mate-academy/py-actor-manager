import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self.db_name.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.db_name.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self.db_name.execute(f"SELECT * FROM {self.table_name}")

        return [Actor(*row) for row in actor_cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.db_name.execute(
            f"UPDATE {self.table_name} SET "
            f"first_name=?, last_name=? WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.db_name.commit()

    def delete(self, pk: int) -> None:
        self.db_name.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk,)
        )
        self.db_name.commit()
