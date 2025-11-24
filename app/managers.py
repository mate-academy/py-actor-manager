import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sql = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT, "
            "last_name TEXT)"
        )

        cur.execute(sql)
        conn.commit()
        conn.close()

    def create(self, first_name: str, last_name: str) -> Actor:
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sql = (
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)"
        )

        cur.execute(sql, (first_name, last_name))
        conn.commit()

        actor_id = cur.lastrowid

        conn.close()

        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sql = f"SELECT id, first_name, last_name FROM {self.table_name}"

        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sql = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?"
        )

        cur.execute(sql, (new_first_name, new_last_name, pk))
        conn.commit()
        conn.close()

    def delete(self, pk: int) -> None:
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sql = f"DELETE FROM {self.table_name} WHERE id = ?"

        cur.execute(sql, (pk,))
        conn.commit()
        conn.close()
