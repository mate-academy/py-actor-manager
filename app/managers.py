import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = sqlite3.connect(db_name)
        self.table_name = table_name
        self.cursor = self.db_name.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.db_name.commit()

    def all(self) -> list[Actor]:
        literary_format = self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in literary_format
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self.db_name.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (pk,)
        )
        self.db_name.commit()

# if __name__ == "__main__":
#     manager = ActorManager(db_name="cinema.db", table_name="actors")
#     manager.create(last_name="Morty", first_name="Smit")
#     print(manager.all())
