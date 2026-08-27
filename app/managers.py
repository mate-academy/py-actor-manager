import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()

    def create(self, first_name, last_name):
        actor = Actor(first_name=first_name, last_name=last_name)

    def all(self):
        self._cursor.execute("SELECT * FROM actor")
        return [Actor(*row) for row in self._cursor]

    def update(self, pk, new_first_name, new_last_name):
        pass

    def delete(self, pk):
        pass