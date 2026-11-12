import sqlite3

from .models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        query = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
        """

        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        query = f"""
            SELECT id, first_name, last_name
            FROM {self.table_name}
        """

        cursor = self.connection.execute(query)
        rows = cursor.fetchall()

        actors = []

        for row in rows:
            actor = Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            )
            actors.append(actor)

        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """

        self.connection.execute(
            query,
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query = f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
        """

        self.connection.execute(query, (pk,))
        self.connection.commit()
