import sqlite3
from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
        self,
        id_update: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, id_update),
        )
        self._connection.commit()

    def delete(self, id_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_delete,)
        )
        self._connection.commit()


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")
# with sqlite3.connect(db_path) as db:
