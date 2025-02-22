import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"
        self.create_table()

    def create_table(self):
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS actors (
                actors_first_name TEXT NOT NULL,
                actors_last_name TEXT NOT NULL ,
                id INTEGER PRIMARY KEY AUTOINCREMENT
            );
            """
        )
        self._connection.commit()

    def create(self, first_name:str, last_name:str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (actors_first_name, actors_last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self,id_to_update:int, name_to_update:str, surname_to_update:str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET actors_first_name = ?, actors_last_name = ? "
            "WHERE id = ? ",
            (name_to_update, surname_to_update, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
