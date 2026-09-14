import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
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
        return Actor(
            id=self.cursor.lastrowid,
            first_name=first_name,
            last_name=last_name
        )

    def all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [
            Actor(
            id=self.row[0],
            title=row[1],
            author=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
        f"UPDATE {self.table_name}"
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk,),
        )
        self.connection.commit()
