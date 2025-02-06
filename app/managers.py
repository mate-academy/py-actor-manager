import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name="cinema.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()


    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')
        self.conn.commit()


    def create(self, first_name: str, last_name: str):
        self.cursor.execute("INSERT INTO actors (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()


    def all(self):
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]


    def update(self, actor_id: int, first_name: str, last_name: str):
        self.cursor.execute("UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
                            (first_name, last_name, actor_id))
        self.conn.commit()


    def delete(self, actor_id: int):
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()


    def close(self):
        self.conn.close()
