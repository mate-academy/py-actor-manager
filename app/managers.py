import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name:str, table_name:str):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self._ensure_table()


    def _ensure_table(self):
        cur= self.conn.cursor()
        cur.execute(
            f" CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, last_name TEXT NOT NULL)"
        )
        self.conn.commit()


    def create(self, first_name, last_name):
        cur = self.conn.cursor()
        cur.execute(
            f" INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",(first_name, last_name)
            )
        self.conn.commit()
        pk = cur.lastrowid
        return pk


    def all(self):
        cur = self.conn.cursor()
        cur.execute(
            f"SELECT * FROM {self.table_name} "
        )
        rows = cur.fetchall()

        actors = [Actor(id = row["id"], first_name = row["first_name"], last_name = row["last_name"]) for row in rows]
        return actors


    def update(self,pk, new_first_name, new_last_name):
        cur = self.conn.cursor()
        cur.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
                    (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk):
        cur = self.conn.cursor()
        cur.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,))
        self.conn.commit()

