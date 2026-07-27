import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.connection = sqlite3.Connection
        self._db_name = db_name
        self._table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {self._table_name} (first_name, last_name)
                VALUES (?, ?)
            """, (first_name, last_name))
            conn.commit()

    def all(self) -> list[Actor]:
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name}")
            rows = cursor.fetchall()

            return [
                Actor(id=row[0], first_name=row[1], last_name=row[2])
                for row in rows
            ]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {self._table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """, (new_first_name, new_last_name, pk))
            conn.commit()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM {self._table_name} WHERE id = ?",
                (pk,)
            )
            conn.commit()
