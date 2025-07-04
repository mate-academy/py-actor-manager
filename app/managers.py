import sqlite3


from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name : str) -> None:
        self._connection = sqlite3.connect(database=db_name)
        self._table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self._table_name} "
                                 f"(first_name, last_name) "
                                 f"VALUES (?, ?)",
                                 (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = (self._connection.execute(f"SELECT * "
                                                  f"FROM {self._table_name}"))
        return [Actor(*row) for row in actors_cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(f"UPDATE {self._table_name} "
                                 f"SET first_name = ? , "
                                 f"last_name = ? WHERE id= ? ",
                                 (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(f"DELETE FROM {self._table_name} "
                                 f"WHERE id=?", (pk,))

    def __exit__(self, exc_type: Exception,
                 exc_val: Exception,
                 exc_tb: Exception) -> None:
        # Close the connection
        if self._connection:
            self._connection.close()
            self._connection = None
