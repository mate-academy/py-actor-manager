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
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            "VALUES(?, ?)", (first_name, last_name))
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    actor = ActorManager()
    actor.delete(2)
    print(actor.all())
