import sqlite3
from typing import List, Tuple

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self.db_name = "actors_db"
        self._connection = sqlite3.connect(f"../{self.db_name}.sqlite")

    def all(self) -> List[Tuple[int, str, str]]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return actors_cursor.fetchall()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
        (new_first_name, new_last_name, id_to_update),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
    manager.create("Courtney", "Miller")
    manager.all()
    manager.update(3, "Courtney", "Topp")
    manager.all()
    manager.delete(3)
    manager.all()
