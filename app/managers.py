import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
""", (first_name, last_name)
        )
        self.conn.commit()
        cursor.close()

    def read(self) -> list[Actor]:
        cursor = self.conn.cursor()
        cursor.execute(
            f"""SELECT id, first_name, last_name
            FROM {self.table_name}
"""
        )
        results = cursor.fetchall()
        cursor.close()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in results
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name=?, last_name=?
            WHERE id=?""",
            (new_first_name, new_last_name, pk),
        )
        self.conn.commit()
        cursor.close()

    def delete(self, pk: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id=?""",
            (pk,)
        )
        self.conn.commit()

        if cursor.rowcount > 0:
            print(f"Register with ID {pk} excluded with success")
        else:
            print(f"Not found any register with ID {pk}.")
        cursor.close()
