import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        base = (f"INSERT INTO {self.table_name} (first_name, last_name) "
                f"VALUES (?, ?)")
        self.cursor.execute(base, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        base = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(base)
        rows = self.cursor.fetchall()
        return [
            Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            for row in rows
        ]

    def update(self, pk: id, new_first_name: str, new_last_name: str) -> None:
        base = (f"UPDATE {self.table_name} SET first_name=?, last_name=? "
                f"WHERE id=?")
        self.cursor.execute(base, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        base = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(base, (pk, ))
        self.conn.commit()
