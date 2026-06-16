import sqlite3
from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

        return Actor(id=cursor.lastrowid,
                     first_name=first_name,
                     last_name=last_name)

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        rows = cursor.fetchall()

        actors = []
        for row in rows:
            actor = Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
            )
            actors.append(actor)
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (new_first_name, new_last_name, pk,)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
