import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connector = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self.connector.execute(f"INSERT INTO {self.table_name} (first_name, last_name)"
                               f"VALUES (?, ?)", (first_name, last_name))
        self.connector.commit()

    def all(self) -> list:
        actors_date = self.connector.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors_date]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.connector.execute(f"UPDATE {self.table_name} SET first_name=?, last_name=?"
                               f"WHERE id=?", (new_first_name, new_last_name, pk))

    def delete(self, pk: int) -> None:
        self.connector.execute(f"DELETE FROM {self.table_name} WHERE id=?", (pk,))
