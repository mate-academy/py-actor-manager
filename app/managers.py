import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._con = sqlite3.connect("cinema.db")
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str):
        self._con.execute(
            f"INSERT INTO {self.table_name}(first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._con.commit()

    def all(self):
        actor_cursor = self._con.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actor_cursor]

    def update(self, id_: int, first_name: str, last_name: str):
        self._con.execute(
            f"UPDATE {self.table_name}"
            " SET first_name=? ,last_name=?"
            " WHERE id=?",
            (first_name, last_name, id_)
        )
        self._con.commit()

    def delete(self, id_: int):
        self._con.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_,)
        )
        self._con.commit()
