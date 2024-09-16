import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update: int, new_value: tuple):
        self._connection.execute(
            f"UPDATE {self.name} "
            "SET first_name= ?, last_name= ? "
            "WHERE id= ?",
            (*new_value, id_to_update)
        )

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.name} "
            f"WHERE id= ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == '__main__':
    manager = ActorManager()
    print(manager.all())
