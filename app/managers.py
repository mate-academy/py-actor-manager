import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("../cinema.sqlite")
        self.cursor = self.conn.cursor()
        self.table_name = "actors"

    def all(self) -> list:
        self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return self.cursor.fetchall()

    def delete(self, id_: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_,)
        )
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f" VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_)
        )
        self.conn.commit()
