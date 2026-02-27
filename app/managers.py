import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.database = db_name
        self.conn = sqlite3.connect(f"{db_name}.db")
        self.table_name = table_name
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id integer PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT
        )""")
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"""INSERT INTO {self.table_name}
            (first_name, last_name)
            VALUES (?, ?)""",
            (first_name, last_name),
        )
        self.conn.commit()

    def all(self) -> list:
        res = self.cursor.execute(f"SELECT id, first_name,"
                                  f" last_name FROM {self.table_name}")
        actors = res.fetchall()
        result = []
        for actor in actors:
            result.append(Actor(actor[0], actor[1], actor[2]))
        return result

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?,
                last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk),
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (pk,),
        )
        self.conn.commit()
