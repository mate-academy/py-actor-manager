import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} "
                            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            f"first_name TEXT , "
                            f"last_name TEXT)")
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        list_of_actors = []
        for row in self.cursor.execute(f"SELECT * FROM {self.table_name}"):
            actor = Actor(row[0], row[1], row[2])
            list_of_actors.append(actor)
        return list_of_actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )

        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()
