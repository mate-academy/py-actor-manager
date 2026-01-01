import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, first_name, last_name FROM actors")
        rows = cursor.fetchall()  # returns a list of tuples

        # convert rows to Actor instances
        actors = [Actor(id=row[0],
                        first_name=row[1],
                        last_name=row[2]) for row in rows]

        return actors  # returns empty list if no rows

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM actors WHERE id = ?",
            (pk,)
        )
        self.conn.commit()
