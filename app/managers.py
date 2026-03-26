import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        query = f"""CREATE TABLE IF NOT EXISTS {table_name}(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
first_name TEXT NOT NULL, 
last_name TEXT NOT NULL)"""
        self.cursor.execute(query)
        self.conn.commit()

    def __del__(self) -> None:
        self.cursor.close()
        self.conn.close()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} VALUES (null, ?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        result = []
        self.cursor.execute(
            f"""
            SELECT id, first_name, last_name
            FROM {self.table_name}
            """
        )
        res = self.cursor.fetchall()
        for i in res:
            result.append(
                Actor(id=i[0], first_name=i[1], last_name=i[2])
            )
        return result

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        self.cursor.execute(
            f"""UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?""",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = {pk}"
        )
        self.conn.commit()
