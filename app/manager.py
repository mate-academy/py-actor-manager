import sqlite3

from models import Actor

class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(r"C:\Users\Новатор 3\PycharmProjects\py-actor-manager\cinema.sqlite")
        self.table_name = "actors"

    def create(self, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?,?)",
            (new_first_name, new_last_name)
        )
        self._connection.commit()


    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self, id_to_change: int, update_first_name: str, update_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (update_first_name, update_last_name, id_to_change)
        )
        self._connection.commit()

    def delete(self, id_to_delete) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
