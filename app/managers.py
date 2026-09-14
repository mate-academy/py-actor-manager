import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f""
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            f"  first_name TEXT NOT NULL,"
            f"  last_name TEXT NOT NULL"
            f") "
            f""
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        return Actor(id=self.cursor.lastrowid, first_name=first_name, last_name=last_name)

    def all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def update(self, primary_key: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, primary_key)
        )
        self.connection.commit()

    def delete(self, primary_key: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (primary_key,),
        )
        self.connection.commit()
