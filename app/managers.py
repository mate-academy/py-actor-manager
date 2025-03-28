import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect('actors.db')
        self.table_name = 'actors'


    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f" VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()


    def all(self) -> list:
        cursor = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [
            Actor(*row) for row in cursor
        ]

    def update(self, id_to_update: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name=?, last_name=?"
            " WHERE id = ? ",
            (first_name, last_name, id_to_update)
        )

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
        (id_to_delete,)
        )

