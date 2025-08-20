import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cur.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        self.cur.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cur.fetchall()
        return [Actor(i[0], i[1], i[2]) for i in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cur.execute(
            f"UPDATE {self.table_name} SET first_name = ?,last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int, ) -> None:
        self.cur.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
