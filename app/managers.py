from app.models import Actor

import sqlite3


class ActorManager:

    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)
        self.cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str):

        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        literary_format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in literary_format_cursor]

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
            f"delete from {self.table_name} where id = ?",
            (pk,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
    manager.delete(4)
    print(manager.all())
