import sqlite3
from madels import Actor



class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self._connection.row_factory = sqlite3.Row

    def all(self):
        actor_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        actors = [
            Actor(id=row["id"], first_name=row["first_name"], last_name=row["last_name"]) for row in actor_cursor.fetchall()
        ]
        return actors

    def create(self, first_name, last_name):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO actors (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        self._connection.commit()
        actor_id = cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def update(self, actor_id, first_name=None, last_name=None):
        if first_name:
            self._connection.execute("UPDATE actors SET first_name = ? WHERE id = ?", (first_name, actor_id))
        if last_name:
            self._connection.execute("UPDATE actors SET last_name = ? WHERE id = ?", (last_name, actor_id))
        self._connection.commit()

    def delete(self, actor_id):
        self._connection.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self._connection.commit()