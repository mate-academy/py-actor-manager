import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.Connection("cinema.db3")
        self.table_name = "actor"

    def all(self):
        actors_list = self.connection.execute("SELECT * FROM actor")
        return [Actor(*actor) for actor in actors_list]

    def create(self, first_name: str, last_name: str):
        self.connection.execute(f"INSERT INTO {self.table_name} "
                                f"(first_name, last_name) VALUES (?, ?)",
                                (first_name, last_name))
        self.connection.commit()

    def update(self, id_for_update: int, first_name: str, last_name: str):
        self.connection.execute(f"UPDATE {self.table_name} SET "
                                f"first_name = ?, last_name = ? WHERE id = ?",
                                (first_name, last_name, id_for_update))
        self.connection.commit()

    def delete(self, id_for_delete: int):
        self.connection.execute(f"DElETE FROM {self.table_name} WHERE id = ?",
                                (id_for_delete,))
        self.connection.commit()
