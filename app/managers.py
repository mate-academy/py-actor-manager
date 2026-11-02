
import sqlite3


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f" VALUES (?, ?)"
        )
        cursor = self._connection.cursor()
        cursor.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self._connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        query = (
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name = ?"
            " WHERE pk = ?"
        )
        cursor = self._connection.cursor()
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE pk = ?"
        cursor = self._connection.cursor()
        cursor.execute(query, (pk,))
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
