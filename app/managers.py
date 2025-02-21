import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.cursor = self.connection.cursor()

    def create(self, **kwargs) -> None:
        self.cursor.execute("SELECT COUNT(*) FROM actors")
        row_count = int(self.cursor.fetchall()[0][0])
        insert_str = "INSERT"
        query = f"{insert_str} INTO actors (id, first_name, last_name) " \
            "VALUES (?, ?, ?)",\
            (row_count + 1, kwargs["first_name"], kwargs["last_name"])
        self.connection.execute(str(query))

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        result = []
        for actor in self.cursor.fetchall():
            result.append(Actor(actor[0], actor[1], actor[2]))
        return result

    def update(self, identifier: int, first_n: str, last_n: str) -> None:
        update_query = ("UPDATE actors SET first_name = (?), last_name = (?) "
                        "WHERE id = (?)", (first_n, last_n, identifier))
        self.cursor.execute(str(update_query))
        self.connection.commit()

    def delete(self, identifier: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (identifier,))
