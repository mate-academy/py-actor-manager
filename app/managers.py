import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> Actor:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        actor_id = self.cur.lastrowid
        self.close_conn()
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cur.fetchall()

        actors = []
        for row in rows:
            actor = Actor(id=row[0], first_name=row[1], last_name=row[2])
            actors.append(actor)
        self.close_conn()
        return actors

    def update(self, pk: int, new_first_name: str,
               new_last_name: str) -> Actor:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()
        self.close_conn()
        return Actor(id=pk, first_name=new_first_name, last_name=new_last_name)

    def delete(self, pk: int) -> None:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.conn.commit()
        self.close_conn()

    def close_conn(self) -> None:
        self.cur.close()
        self.conn.close()
