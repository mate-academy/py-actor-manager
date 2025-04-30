import sqlite3
import os

from app.models import Actor
from typing import List


class ActorManager:
    def __init__(self,
                 db_name: str = None,
                 table_name: str = "actors_info"
                 ) -> None:
        if db_name is None:
            project_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            db_path = os.path.join(project_dir, "actors.sqlite")
            self.db_name = db_path
        else:
            self.db_name = db_name

        self.table_name = table_name
        self.__connection = sqlite3.connect(self.db_name)

    def all(self) -> List[Actor]:
        actor_cursor = self.__connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def create(self,
               *,
               first_name: str,
               last_name: str) -> None:
        self.__connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.__connection.commit()

    def update(self,
               *,
               pk: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.__connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ? , last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self.__connection.commit()

    def delete(self, pk: int) -> None:
        self.__connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (pk,)
        )
        self.__connection.commit()
