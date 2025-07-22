import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str = "actors_data_db.sqlite", table_name: str = "actors"):
        self._connection = sqlite3.connect(db_name)
        #self.db_name = "actors_data_db.sqlite"
        self.table_name = table_name

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT* FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self._connection.commit()



if __name__ == "__main__":
    manager = ActorManager()
    manager.create("Antuan", "Brizard")
    print(manager.all())
