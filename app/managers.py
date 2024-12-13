import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self,
               first_name: str,
               last_name: str
               ) -> None:
        query = f"""
        INSERT INTO {self.table_name} (first_name, last_name)
        VALUES (?, ?);
        """
        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> List[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(self,
               id_to_update: int,
               first_name: str,
               last_name: str
               ) -> None:
        query = f"""
        UPDATE {self.table_name}
        SET first_name = ?, last_name = ?
        WHERE id = ?;
        """
        self._connection.execute(query, (first_name, last_name, id_to_update))
        self._connection.commit()

    def delete(self,
               id_to_delete: int
               ) -> None:
        query = f"""
        DELETE FROM {self.table_name}
        WHERE id = ?;
        """
        self._connection.execute(query, (id_to_delete,))
        self._connection.commit()
