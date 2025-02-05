import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_path: str, table_name: str) -> None:
        self._db_path = db_path
        self._table_name = table_name
        self.conn = sqlite3.connect(self._db_path)

    def all(self) -> list[Actor]:
            cursor = self.conn.execute(
                f"""
                SELECT *
                FROM {self._table_name}
                """
            )
            return cursor.fetchall()

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self._table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def update(self, actor_id: int,
               first_name: str = None,
               last_name: str = None) -> None:
        updates = []
        params = []
        if first_name:
            updates.append("first_name = ?")
            params.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            params.append(last_name)

        params.append(actor_id)
        set_clause = ", ".join(updates)

        if set_clause:  # Only proceed if there are updates to be made
            self.conn.execute(
                f"UPDATE {self._table_name} SET {set_clause} WHERE id = ?",
                tuple(params)
            )
            self.conn.commit()

    def delete(self, actor_id: int) -> None:

        self.conn.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (actor_id,)
        )
        self.conn.commit()

    def __del__(self) -> None:
        if self.conn:
            self.conn.close()
