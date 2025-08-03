import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    conn = None

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        ActorManager.conn = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cursor = ActorManager.conn.cursor()
        cursor.execute(f"INSERT INTO {self.table_name} "
                       f"(first_name, last_name) VALUES(?, ?)",
                       (first_name, last_name))
        ActorManager.conn.commit()

    def all(self) -> list:
        ls = []
        cursor = ActorManager.conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = cursor.fetchall()

            for row in rows:
                actor = Actor(*row)
                ls.append(actor)

            return ls
        except sqlite3.Error:
            return []

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = ActorManager.conn.cursor()
        cursor.execute(f"UPDATE {self.table_name} "
                       f"SET first_name= ?, last_name= ? WHERE id = ?",
                       (new_first_name, new_last_name, pk))
        ActorManager.conn.commit()

    def delete(self, pk: int) -> None:
        cursor = ActorManager.conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
