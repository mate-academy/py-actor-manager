import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"""INSERT INTO {self.table_name} (first_name,
                    last_name) VALUES (?, ?)""",
            (first_name, last_name)
        )
        self.conn.commit()
        new_id = self.cursor.lastrowid

        return Actor(new_id, first_name, last_name)

    def all(self) -> list:
        result = self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        ).fetchall()
        return [Actor(*row) for row in result]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"""UPDATE {self.table_name} SET first_name = ?, last_name = ?
                    WHERE id = ?""",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"""DELETE FROM {self.table_name} WHERE id = ?""",
            (pk,)
        )
        self.conn.commit()
