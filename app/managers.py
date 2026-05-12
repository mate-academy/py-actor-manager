import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name}"
            f" ("
            f" id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f" first_name TEXT, "
            f" last_name TEXT"
            f")"
        )
        self.cursor.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        results = self.cursor.fetchall()
        self.conn.commit()

        return [Actor(result[0], result[1], result[2]) for result in results]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name}"
            f" WHERE id = ?",
            (pk,)
        )
        self.conn.commit()

    def close(self) -> None:
        self.cursor.close()
