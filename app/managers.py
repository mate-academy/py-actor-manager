import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cur.execute(f"INSERT INTO {self.table_name}"
                         f"(first_name, last_name) "
                         "VALUES (?,?)", (first_name, last_name))
        self.con.commit()

    def all(self) -> list:
        res = self.cur.execute(f"SELECT id, first_name, last_name "
                               f"FROM {self.table_name}")
        rows = res.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cur.execute(f"UPDATE {self.table_name} "
                         f"SET first_name = ?, last_name = ? WHERE id = ?",
                         (new_first_name, new_last_name, pk))
        self.con.commit()

    def delete(self, pk: int) -> None:
        self.cur.execute(f"DELETE FROM {self.table_name} "
                         f"WHERE id = ?", (pk,))
        self.con.commit()
