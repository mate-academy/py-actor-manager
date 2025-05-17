import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)

    def all(self) -> list:
        curs = self._connection.execute(
            f"select * from {self.table_name}"
        )
        return [Actor(*row) for row in curs]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"insert into {self.table_name} "
            f"(first_name, last_name) values (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"Update {self.table_name} "
            "set first_name = ?, "
            "last_name = ? "
            "where id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"delete from {self.table_name} "
            "where id = ?",
            (pk,)
        )
        self._connection.commit()
