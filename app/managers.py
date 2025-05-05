import sqlite3
from typing import Callable, List

from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(
            self,
            first_name: str,
            last_name: str,
    ) -> Callable:
        new_actor = Actor(
            id=None,
            first_name=first_name,
            last_name=last_name,
        )

        query = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"

        self.cursor.execute(query, (new_actor.first_name, new_actor.last_name))

        self.conn.commit()

        new_actor.id = self.cursor.lastrowid

        return new_actor

    def all(self) -> List[Actor]:

        query = f"SELECT * FROM {self.table_name}"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        actors = [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

        return actors

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str,
    ) -> None:

        query = f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?"

        self.cursor.execute(query, (new_first_name, new_last_name, pk))

        self.conn.commit()

    def delete(self, pk: int) -> None:

        query = f"DELETE FROM {self.table_name} WHERE id=?"

        self.cursor.execute(query, (pk,))

        self.conn.commit()
