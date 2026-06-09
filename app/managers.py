import sqlite3

from typing import List

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # create table here

    def _create_table(self) -> None:
        self.cursor.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
            """
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        # Insert new actor, return the created Actor with id
        self._create_table()
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        new_id = self.cursor.lastrowid
        self.connection.commit()
        return Actor(id=new_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        rows = cursor.fetchall()

        # Convert each row to an Actor instance
        actors = []
        for row in rows:
            actor = Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            actors.append(actor)

        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        # Update by id
        self.cursor.execute(
            f"UPDATE {self.table_name} SET "
            "first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = {pk}"
        )
        self.connection.commit()
