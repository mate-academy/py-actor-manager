import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> str:
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_,)
        )
        self._connection.commit()

    def all(self) -> None:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name_: str,
            new_last_name_: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, "
            f"last_name = ? WHERE id= ?",
            (new_first_name_, new_last_name_, id_to_update, )
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM  {self.table_name} WHERE id=?", (id_to_delete, )
        )
        self._connection.commit()
