import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cu = self.connection.cursor()

        query = (f"INSERT INTO {self.table_name} (first_name, last_name) "
                 f"VALUES (?, ?)")
        cu.execute(query, (first_name, last_name))

        self.connection.commit()

    def all(self) -> list[Actor]:
        cu = self.connection.cursor()

        query = f"SELECT * FROM {self.table_name}"

        result = []
        for row in cu.execute(query):
            result.append(Actor(row[0], row[1], row[2]))
        return result

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cu = self.connection.cursor()

        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? "
                 f"WHERE id = ?")

        cu.execute(query, (new_first_name, new_last_name, pk))

        self.connection.commit()

    def delete(self, pk: int) -> None:
        cu = self.connection.cursor()

        query = f"DELETE FROM {self.table_name} WHERE id = ?"

        cu.execute(query, (pk,))

        self.connection.commit()
