import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) "
                 f"VALUES (?, ?)")
        self._connection.execute(query, (first_name, last_name, ))
        self._connection.commit()

    def all(self) -> list:
        query = f"SELECT * FROM {self.table_name}"
        result_cursor = self._connection.execute(query)
        return [Actor(*row) for row in result_cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? "
                 f"WHERE id = ? ")
        self._connection.execute(query, (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._connection.execute(query, (pk, ))
        self._connection.commit()
