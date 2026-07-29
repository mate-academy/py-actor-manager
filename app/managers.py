import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self._cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        new_id = self._cursor.lastrowid
        assert isinstance(new_id, int)
        self._connection.commit()

        actor = Actor(
            id=new_id,
            first_name=first_name,
            last_name=last_name
        )

        return actor

    def all(self) -> list[Actor]:
        self._cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        rows = self._cursor.fetchall()
        return [
            Actor(*row) for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
