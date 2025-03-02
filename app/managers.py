import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._connection.row_factory = sqlite3.Row

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute("SELECT * FROM actors")
        actors = [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"]
            )
            for row in actor_cursor.fetchall()
        ]
        return actors

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()
        actor_id = cursor.lastrowid
        return Actor(
            id=actor_id,
            first_name=first_name,
            last_name=last_name
        )

    def update(self, actor_id: int, first_name: str = None, last_name: str = None) -> None:
        if first_name:
            self._connection.execute(
                "UPDATE actors SET first_name = ? WHERE id = ?",
                (first_name, actor_id)
            )
        if last_name:
            self._connection.execute(
                "UPDATE actors SET last_name = ? WHERE id = ?",
                (last_name, actor_id)
            )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
