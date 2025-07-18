import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name: str = db_name
        self.table_name: str = table_name
        self._create_table()

    def _create_table(self) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "first_name TEXT NOT NULL, "
                "last_name TEXT NOT NULL)"
            )

            conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                ''',
                (first_name, last_name),
            )
            conn.commit()

    def all(self) -> List[Actor]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                SELECT id, first_name, last_name
                FROM {self.table_name}
                '''
            )
            rows = cursor.fetchall()
            return [
                Actor(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                )
                for row in rows
            ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                ''',
                (new_first_name, new_last_name, pk),
            )
            conn.commit()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                DELETE FROM {self.table_name}
                WHERE id = ?
                ''',
                (pk,),
            )
            conn.commit()
