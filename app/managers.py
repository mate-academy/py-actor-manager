import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list:
        actors = self.conn.execute(
            f"SELECT * FROM {self.table}"
        )
        return [Actor(*row) for row in actors]

    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (first_name, last_name, id_to_update)
        )
        self.conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table} WHERE id=?",
            (id_to_delete,)
        )
        self.conn.commit()

    def delete_all(self) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table}"
        )
        self.conn.commit()
