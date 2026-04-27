import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.db_table = table_name

        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.db_table} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL)""")
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        insert_query = f"""INSERT INTO {self.db_table} (first_name, last_name)
                            VALUES (?, ?)"""
        cursor = self.connection.cursor()
        cursor.execute(insert_query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.db_table}")
        rows = cursor.fetchall()
        return [
            Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        update_query = f"""UPDATE {self.db_table}
                            SET first_name = ?, last_name = ?
                            WHERE id = ?"""
        cursor = self.connection.cursor()
        cursor.execute(update_query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        delete_query = f"""DELETE FROM {self.db_table} WHERE id = ?"""
        cursor = self.connection.cursor()
        cursor.execute(delete_query, (pk,))
        self.connection.commit()
