import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def all(self) -> list[Actor]:
        cinema_cursor = self._connection.execute(
            f"""
                SELECT *
                FROM {self._table_name}
            """
        )
        return [Actor(*row) for row in cinema_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
                INSERT INTO {self._table_name} (first_name, last_name)
                VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
            self,
            update_id: int,
            first_name: str = None,
            last_name: str = None
    ) -> None:
        self._connection.execute(
            f"""
                UPDATE {self._table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """,
            (first_name, last_name, update_id)
        )
        self._connection.commit()

    def delete(self, delete_id: int) -> None:
        self._connection.execute(
            f"""
                    DELETE FROM {self._table_name}
                    WHERE id = ?
            """,
            (delete_id,)
        )
        self._connection.commit()
