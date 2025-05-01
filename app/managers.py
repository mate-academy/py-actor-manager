import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("../cinema.sqlite")

# C - create
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

# ALL
    def all(self) -> list[Actor]:
        results = self._connection.execute(
            f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in results]

# U - update
    def udpate(self, new_first_name: str,
               new_last_name: str, id_to_delete: int) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?, last_name = ?, WHERE id = ?",
            (new_first_name, new_last_name, id_to_delete)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    module_actor = ActorManager()
    print(module_actor.udpate("Leonardo", "DiCaprio", 1))
    module_actor.delete(6)
