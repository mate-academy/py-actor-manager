import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?,?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str,
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update),
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?", (actor_id,)
        )
        self._connection.commit()
