import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.connection.cursor()
        query = (
            'INSERT INTO "{}" '
            "(first_name, last_name) VALUES (?, ?)"
        ).format(self.table_name)
        cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        query = (
            'SELECT id, first_name, last_name FROM "{}"'
        ).format(self.table_name)
        cursor.execute(query)
        rows = cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.connection.cursor()
        query = (
            'UPDATE "{}" '
            "SET first_name = ?, last_name = ? WHERE id = ?"
        ).format(self.table_name)
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self.connection.cursor()
        query = 'DELETE FROM "{}" WHERE id = ?'.format(self.table_name)
        cursor.execute(query, (pk,))
        self.connection.commit()
