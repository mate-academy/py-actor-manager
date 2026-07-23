import sqlite3
from app.models import Actor



class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> Actor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                );
            """)
            query = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?);"
            cursor.execute(query, (first_name, last_name))
            generated_id = cursor.lastrowid

        return Actor(id=generated_id, first_name=first_name, last_name=last_name)  # <-- poza with

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        query = f"SELECT id, first_name, last_name FROM {self.table_name};"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:

        with self.connection:
            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?;"
            cursor.execute(query, (new_first_name, new_last_name, pk))

    def delete(self, pk: int) -> None:

        with self.connection:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id = ?;"
            cursor.execute(query, (pk,))


