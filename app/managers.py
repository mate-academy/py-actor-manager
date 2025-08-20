# app/managers.py
import sqlite3
from app.models import Actor

class ActorManager:
    def __init__(self, db_name: str = "actors.db", table_name: str = "actors"):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row  # rekordy jak słowniki

        # Tworzymy tabelę, jeśli nie istnieje
        self.conn.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )"""
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

    # --- CREATE ---
    def create(self, first_name: str, last_name: str) -> Actor:
        cur = self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        new_id = cur.lastrowid
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    # --- ALL ---
    def all(self) -> list[Actor]:
        cur = self.conn.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name} ORDER BY id"
        )
        rows = cur.fetchall()
        return [Actor(id=row["id"], first_name=row["first_name"], last_name=row["last_name"]) for row in rows]

    # --- UPDATE ---
    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        cur = self.conn.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()
        return cur.rowcount > 0

    # --- DELETE ---
    def delete(self, pk: int) -> bool:
        cur = self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk,)
        )
        self.conn.commit()
        return cur.rowcount > 0
