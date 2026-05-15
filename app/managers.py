import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_conn = sqlite3.connect(db_name)
        self.cursor = self.db_conn.cursor()
        self.table_name = table_name

        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT, last_name TEXT)"
        )

        self.db_conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES ('{first_name}', '{last_name}')"
        )
        self.db_conn.commit()

    def all(self) -> list[Actor]:
        actors = []
        self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        rows = self.cursor.fetchall()
        for row in rows:
            actors.append(Actor(row[0], row[1], row[2]))

        return actors

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = '{new_first_name}', "
            f"last_name = '{new_last_name}' "
            f"WHERE id = {pk}"
        )
        self.db_conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {pk}"
        )
        self.db_conn.commit()
