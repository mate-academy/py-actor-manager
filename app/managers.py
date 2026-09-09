import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name),
        )

        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
            SELECT id, first_name, last_name
            FROM {self.table_name}
            """
        )

        actors = cursor.fetchall()

        return [
            Actor(
                id=actor[0],
                first_name=actor[1],
                last_name=actor[2],
            )
            for actor in actors
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk),
        )

        self.connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (pk,),
        )

        self.connection.commit()
