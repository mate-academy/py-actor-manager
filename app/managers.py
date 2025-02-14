import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sql")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("INSERT INTO actors (first_name, last_name)"
                            "VALUES (?, ?)", (first_name, last_name))
        self.connection.commit()

    def all(self) -> list:
        self.cursor.execute("SELECT * FROM actors")
        return self.cursor.fetchall()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute("UPDATE actors SET first_name = ?,"
                            " last_name = ? WHERE id = ?",
                            (first_name, last_name, id))
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.connection.commit()
