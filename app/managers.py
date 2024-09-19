import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("app/cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list:
        table_data = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in table_data]

    def update(
        self,
        id_to_update: int,
        first_name_to_update: str,
        last_name_to_update: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name_to_update, last_name_to_update, id_to_update),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()
