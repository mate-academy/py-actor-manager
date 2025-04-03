import sqlite3


from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")

        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:
        output = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in output]

    def update(self, id_to_update: int,
               new_first_name: str, new_last_name: str) -> None:

        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = (?), last_name = (?) WHERE id = (?)")
        self._connection.execute(
            query, (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = (?)"
        self._connection.execute(query, (id_to_delete,))
        self._connection.commit()
