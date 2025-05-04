import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.db")
        self._cursor = self._connection.cursor()

    def all(self):
        self._cursor.execute(
            "SELECT id, first_name, last_name FROM actors"
        )
        rows = self._cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows
                ]

    def create(self, first_name, last_name):
        self._cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES(?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._cursor.execute(
            "DELETE FROM actors WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    actor = ActorManager()
    actor.update(3, "Orlando", "Blum")

    print(actor.all())
