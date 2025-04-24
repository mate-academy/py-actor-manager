import sqlite3

from app.models import Actor


class ActorManagers:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.table_name}"
                                 f" (first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name))

        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(f"SELECT * FROM "
                                                f"{self.table_name}")
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 f"SET first_name = ?, last_name = ? "
                                 f"WHERE id = ?",
                                 (first_name, last_name, id_to_update))

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 f" WHERE id = ?", (id_to_delete,))

        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManagers()
    print(manager.update(5, "1drhdhdtj", "123"))
    manager.delete(6)
