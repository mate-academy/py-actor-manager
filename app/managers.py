
import sqlite3

from app.models import Actor


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

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self._connection.cursor()
        cursor.execute(query)

        actors = cursor.fetchall()

        return [
            Actor(
                id=actor[0],
                first_name=actor[1],
                last_name=actor[2]
            )
            for actor in actors
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        query = (
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name = ?"
            " WHERE id = ?"
        )
        cursor = self._connection.cursor()
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        cursor = self._connection.cursor()
        cursor.execute(query, (pk,))
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
