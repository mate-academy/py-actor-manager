import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> None:
        actors_list = []
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        for row in rows:
            actor = Actor(id=row[0], first_name=row[1], last_name=row[2])
            actors_list.append(actor)

        return actors_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name=?, last_name=?"
            f" WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk,)
        )
        self.connection.commit()
