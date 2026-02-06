import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        new_list = []
        for row in cursor:
            row1 = Actor(id=row[0], first_name=row[1], last_name=row[2])
            new_list.append(row1)
        return new_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET "
            f"first_name = ?, last_name = ? WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (pk, )
        )
        self._connection.commit()
