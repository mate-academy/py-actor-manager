import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.connect = sqlite3.connect(self.db_name)

        self.cursor = self.connect.cursor()

        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                            f"{self.table_name}"
                            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            f"first_name TEXT, last_name TEXT) ")

        self.connect.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name}"
                            f" (first_name, last_name) VALUES (?, ?)",
                            (first_name, last_name))

        self.connect.commit()

    def all(self) -> list:
        read_table = self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = read_table.fetchall()
        if not rows:
            return []
        actors = [Actor(id=row[0],
                        first_name=row[1],
                        last_name=row[2]) for row in rows]
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(f"UPDATE {self.table_name}"
                            f" SET first_name = ?, "
                            f" last_name = ?"
                            f" WHERE id = ? ",
                            (new_first_name, new_last_name, pk)
                            )
        self.connect.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(f"""
        DELETE FROM {self.table_name}
        WHERE id = ?""", (pk,)
        )
        self.connect.commit()
