import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._initialize_table()

    def _initialize_table(self) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
            """)
            conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
            """, (first_name, last_name))
            actor_id = cursor.lastrowid
            conn.commit()
            return Actor(
                id=actor_id, first_name=first_name, last_name=last_name
            )

    def all(self) -> list[Actor]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                SELECT id, first_name, last_name FROM {self.table_name}
            """)
            rows = cursor.fetchall()
            actors = []
            for row in rows:
                actor = Actor(id=row[0], first_name=row[1], last_name=row[2])
                actors.append(actor)
            return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """, (new_first_name, new_last_name, pk))
            conn.commit()
            return cursor.rowcount > 0

    def delete(self, pk: int) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
            """, (pk,))
            conn.commit()
            return cursor.rowcount > 0
