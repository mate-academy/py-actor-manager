import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name)
        )
        self.conn.commit()

    def update(self, first_name: str, last_name: str, actor_id: int) -> None:
        if first_name:
            self.cursor.execute(
                "UPDATE actors "
                "SET first_name = ? WHERE id = ?", (first_name, actor_id)
            )
        if last_name:
            self.cursor.execute(
                "UPDATE actors "
                "SET last_name = ? WHERE id = ?", (last_name, actor_id)
            )
        self.conn.commit()

    def all(self) -> List[Actor]:
        actors = (self.cursor.execute("SELECT * FROM actors").fetchall())
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2])
                for row in actors]

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self.conn.commit()

    def close_connection(self) -> None:
        self.conn.close()
