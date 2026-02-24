import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.db_name = db_name
        self.table_name = table_name
        self.connection.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
        """)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) "
                f"VALUES (?, ?);",
                (first_name, last_name),
            )
            return Actor(
                id=cursor.lastrowid, first_name=first_name, last_name=last_name
            )

    def all(self) -> list[Actor]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                f"SELECT id, first_name, last_name FROM {self.table_name};",
            )
            rows = cursor.fetchall()
            return [
                Actor(id=row[0], first_name=row[1], last_name=row[2])
                for row in rows
            ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> Actor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? "
                f"WHERE id = ?;",
                (new_first_name, new_last_name, pk),
            )
            return Actor(
                id=pk, first_name=new_first_name, last_name=new_last_name
            )

    def delete(self, pk: int) -> None:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?;",
                (pk,),
            )

    def __enter__(self) -> "ActorManager":
        return self

    def __exit__(self, exc_type: type, exc_val: type, exc_tb: type) -> None:
        self.connection.close()
