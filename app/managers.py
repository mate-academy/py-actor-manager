import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._conection = sqlite3.connect(db_name)
        self._tabel_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._conection.execute(
            f"INSERT INTO {self._tabel_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conection.commit()

    def all(self) -> list:
        actor_cursor = self._conection.execute(
            f"SELECT * FROM {self._tabel_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self,
               pk: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._conection.execute(
            f"UPDATE {self._tabel_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self._conection.commit()

    def delete(self, pk: int) -> None:
        self._conection.execute(
            f"DELETE FROM {self._tabel_name} "
            f"WHERE id=?",
            (pk,)
        )
        self._conection.commit()
