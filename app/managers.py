import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> int:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?,?)")
        cursor = self.conn.execute(query, (first_name, last_name))
        self.conn.commit()
        return cursor.lastrowid

    def all(self) -> list:
        query = f"SELECT * FROM {self.table_name}"
        rows = self.conn.execute(query).fetchall()
        return [Actor(row["id"], row["first_name"], row["last_name"])
                for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (f"UPDATE {self.table_name} SET "
                 f"first_name = ?, last_name = ? WHERE id = ?")
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = {pk}"
        self.conn.execute(query)
        self.conn.commit()
