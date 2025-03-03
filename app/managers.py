import sqlite3

from models import Actor


class ActorManager:
    def __init__(self, db_name: str="cinema_db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
         self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
         self.conn.commit()

    def create(self, first_name: str, last_name: str):
        self.cursor.execute("INSERT INTO actors (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self):
        self.cursor.execute("SELECT id, first_name, last_name FROM actors")
        rows = self.cursor.fetchall()
        actors = []
        for row in rows:
            actors.append(Actor(id=row[0], first_name=row[1], last_name=row[2]))
        return actors

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self.cursor.execute("UPDATE actors SET first_name=?, last_name=? WHERE id=?", (first_name, last_name, id_to_update))
        self.conn.commit()

    def delete(self, id_to_delete: int):
        self.cursor.execute("DELETE FROM actors WHERE id=?", (id_to_delete,))
        self.conn.commit()