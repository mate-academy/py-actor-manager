import sqlite3

from app.models import Actor


# add manager here


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        # Biztosítjuk, hogy a tábla létezzen az inicializáláskor
        self.connection.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str):
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.execute(query)
        # Az adatbázisból érkező sorokat Actor példányokká alakítjuk
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor.fetchall()
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str):
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self.connection.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(query, (pk,))
        self.connection.commit()
