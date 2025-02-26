import sqlite3
from typing import List


class Actor:
    def __init__(self, id: int, name: str, movie: str) -> None:
        self.id = id
        self.name = name
        self.movie = movie


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("<database_path>")
        self.cursor = self.conn.cursor()

    def create(self, id: int, name: str, movie: str) -> None:
        query = "INSERT INTO actors (id, name, movie) VALUES (?, ?, ?)"
        self.cursor.execute(query, (id, name, movie))
        self.conn.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], name=row[1], movie=row[2]) for row in rows]

    def update(self, id: int, name: str, movie: str) -> None:
        query = "UPDATE actors SET name = ?, movie = ? WHERE id = ?"
        self.cursor.execute(query, (name, movie, id))
        self.conn.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.conn.commit()
