import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        actor_list = cursor.fetchall()
        return [Actor(*actor) for actor in actor_list]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self.conn.commit()
