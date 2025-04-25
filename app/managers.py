import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name="cinema.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.table_name = "actors"
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
            """
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self.connection.commit()
        actor_id = self.cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(
        self,
        actor_id: int,
        first_name: str = None,
        last_name: str = None
    ) -> bool:
        if first_name:
            self.cursor.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?
                WHERE id = ?
                """,
                (first_name, actor_id),
            )
        if last_name:
            self.cursor.execute(
                f"""
                UPDATE {self.table_name}
                SET last_name = ?
                WHERE id = ?
                """,
                (last_name, actor_id),
            )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete(self, actor_id: int) -> bool:
        self.cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (actor_id,),
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def __del__(self):
        self.connection.close()
