import sqlite3


from models import Actor

class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("/Users/dimon/projects/py-actor-manager/cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> Actor:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor (* spisok) for spisok in actor_cursor
        ]

    def update(self, id_new: int, first_name_new: str, last_name_new: str) -> Actor:
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (id_new, first_name_new, last_name_new)
        )
        self._connection.commit()

    def delete(self, id_to_delete) -> Actor:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()