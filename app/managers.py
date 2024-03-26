import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        sql = "INSERT INTO actors" \
              "(first_name,last_name) VALUES (?,?)"
        self.connect.execute(sql, (first_name, last_name))
        self.connect.commit()

    def all(self) -> None:
        actors = self.connect.execute("SELECT * FROM actors")
        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        sql = "UPDATE actors " \
              "SET first_name = ?, last_name = ? " \
              "WHERE id = ?"
        self.connect.execute(sql, (first_name, last_name, id,))
        self.connect.commit()

    def delete(self, id: int) -> None:
        sql = "DELETE FROM actors WHERE id = ?"
        self.connect.execute(sql, (id,))
        self.connect.commit()
