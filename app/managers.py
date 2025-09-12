import sqlite3
from app.models import Actor

class ActorManager:
    def __init__(self, db_name: str, table_name: str = "actors"):
        self.db_name = db_name
        self.table_name = table_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    # CREATE
    def create(self, first_name: str, last_name: str) -> Actor:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )
            conn.commit()
            new_id = cur.lastrowid
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    # READ ALL
    def all(self) -> list[Actor]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT id, first_name, last_name FROM {self.table_name}")
            rows = cur.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    # UPDATE
    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        with self._connect() as conn:
            conn.execute(
                f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
                (new_first_name, new_last_name, pk),
            )
            conn.commit()

    # DELETE
    def delete(self, pk: int) -> None:
        with self._connect() as conn:
            conn.execute(
                f"DELETE FROM {self.table_name} WHERE id=?",
                (pk,),
            )
            conn.commit()
