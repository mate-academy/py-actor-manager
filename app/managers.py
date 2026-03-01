import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        sql = (f"INSERT INTO {self.table_name} "
               f"(first_name, last_name) VALUES (?, ?)")
        self._connection.execute(sql, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:
        sql = f"SELECT * FROM {self.table_name}"
        cursor = self._connection.execute(sql)
        rows = cursor.fetchall()
        return [Actor(row[0], row[1], row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql = (
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ")
        self._connection.execute(sql, (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ? "
        self._connection.execute(sql, (pk,))
        self._connection.commit()
