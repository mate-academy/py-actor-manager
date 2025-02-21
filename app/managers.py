import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.cursor = self.connection.cursor()

    def create(self, **kwargs) -> None:
        self.cursor.execute("SELECT COUNT(*) FROM actors")
        row_count = int(self.cursor.fetchall()[0][0])
        print(row_count)
        self.connection.execute("INSERT INTO actors "
                                "(id, first_name, last_name) "
                                f"VALUES (?, ?, ?)",
                                (row_count + 1,
                                 kwargs["first_name"],
                                 kwargs["last_name"]))

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        result = []
        for actor in self.cursor.fetchall():
            result.append(Actor(actor[0], actor[1], actor[2]))
        return result

    def update(self, identifier: int, first_n: str, last_n: str) -> None:
        update_query = (f"UPDATE actors "
                        f"SET first_name = '{first_n}', last_name = '{last_n}'"
                        f" WHERE id = {identifier}")
        print(update_query)
        self.cursor.execute(update_query)

    def delete(self, identifier: int) -> None:
        self.cursor.execute(f"DELETE FROM actors WHERE id = {identifier}")
