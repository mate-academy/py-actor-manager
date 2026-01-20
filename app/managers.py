import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT
            )
        """)
        self.conn.commit()


    def create(self, first_name, last_name):
        sql = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        self.cursor.execute(sql, (first_name, last_name))
        self.conn.commit()


    def all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        actors = []
        for actor in rows:
            actors.append(Actor(
                id=actor[0],
                first_name=actor[1],
                last_name=actor[2]
            ))
        return actors


    def update(self, pk, new_first_name, new_last_name,):
        sql = f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?"
        self.cursor.execute(sql, (new_first_name, new_last_name, pk))
        self.conn.commit()


    def delete(self, pk):
        sql = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(sql, (pk,))
        self.conn.commit()
