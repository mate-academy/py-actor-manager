import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connector = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connector.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (
                first_name,
                last_name,
            ),
        )
        self._connector.commit()

    def all(self) -> list:
        actor_cursor = self._connector.execute(
            f"SELECT * " f"FROM {self.table_name}"
        )
        return [Actor(*item) for item in actor_cursor]

    def update(self, pk: int, first_name: str, last_name: str) -> None:
        self._connector.execute(
            f"UPDATE FROM {self.table_name} "
            "SET first_name=?, last_name=? WHERE id=?",
            (
                first_name,
                last_name,
                pk,
            ),
        )
        self._connector.commit()

    def delete(self, pk: int) -> None:
        self._connector.execute(
            f"DELETE FROM {self.table_name} WHERE id=?", (pk,)
        )
        self._connector.commit()
