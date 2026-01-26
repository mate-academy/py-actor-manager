import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
first_name TEXT NOT NULL, last_name TEXT NOT NULL) """
        self.cursor.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list:
        self.cursor.execute(
            f"""
            SELECT * FROM {self.table_name}
            """
        )
        rows = self.cursor.fetchall()

        actors = []
        for row in rows:
            row = Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            actors.append(row)
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f"""
            UPDATE {self.table_name} 
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"""
            DELETE FROM {self.table_name} 
            WHERE id = ?
            """,
            (pk,)
        )
        self.connection.commit()
