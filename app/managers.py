import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self.actor_db_connect = sqlite3.connect("../cinema.sqlite")
        self.db_name = "actors"

    def create(self, first_name, last_name):
        self.actor_db_connect.execute(
            f"INSERT INTO {self.db_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self.actor_db_connect.commit()

    def update(self, actor_id, first_name, last_name):
        self.actor_db_connect.execute(
            f"UPDATE {self.db_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (first_name, last_name, actor_id)
        )

        self.actor_db_connect.commit()

    def all(self):
        actor_db_cursor = self.actor_db_connect.execute(
            f"SELECT * FROM {self.db_name}"
        )

        return [Actor(*actor) for actor in actor_db_cursor]

    def delete(self, actor_id):
        self.actor_db_connect.execute(
            f"DELETE FROM {self.db_name} WHERE id = ?",
            (actor_id,)
        )

        self.actor_db_connect.commit()
