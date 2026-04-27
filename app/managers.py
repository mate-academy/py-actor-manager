import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conneciton = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._conneciton.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)", (first_name, last_name)
        )
        self._conneciton.commit()

    def all(self) -> list[Actor]:
        return [Actor(*row) for row in self._conneciton.execute(
            f"SELECT * FROM {self.table_name}"
        )]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._conneciton.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?", (new_first_name, new_last_name, pk)
        )
        self._conneciton.commit()

    def delete(self, pk: int) -> None:
        self._conneciton.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?", (pk,)
        )
        self._conneciton.commit()
