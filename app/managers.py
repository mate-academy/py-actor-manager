import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
                INSERT INTO {self.table_name}
                (first_name, last_name)
                VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
                SELECT *
                FROM {self.table_name}
            """
        )

        rows = cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?,
                last_name = ?
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
