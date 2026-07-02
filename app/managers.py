import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str = "cinema.sqlite",
            table_name: str = "actors"
    ) -> None:
        self.connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def all(self) -> List[Actor]:
        cursor = self.connection.execute(
            "select * from actors"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def delete(self, pk: int) -> None:
        self.connection.execute(
            "delete from actors where id = ?", (pk,)
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "insert into actors (first_name, last_name)"
            " values (?, ?)", (first_name, last_name)
        )
        self.connection.commit()

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.connection.execute(
            "update actors set first_name = ?, last_name = ?"
            " where id = ?", (new_first_name, new_last_name, pk)
        )
        self.connection.commit()
