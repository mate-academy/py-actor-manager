import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) "
                 f"VALUES (?, ?)")
        self.conn.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        actors = self.conn.execute("SELECT * FROM actors").fetchall()
        return [Actor(*actor) for actor in actors]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name=?, last_name=? "
                 f"WHERE id=?")
        self.conn.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        query = (f"DELETE FROM {self.table_name} "
                 f"WHERE id=?")
        self.conn.execute(query, (pk,))
        self.conn.commit()
