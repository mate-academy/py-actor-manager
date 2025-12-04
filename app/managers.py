import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str, ) -> None:
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name
        self.table_name = table_name
        cursor = self.conn.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT, last_name TEXT) ")

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO {self.table_name} "
                       f"(first_name, last_name) VALUES (?, ?)",
                       (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, first_name, "
                       f"last_name FROM {self.table_name}")
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append(Actor(id=row[0], first_name=row[1], last_name=row[2]))
        return data

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.conn.commit()
