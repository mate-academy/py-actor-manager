import sqlite3
from typing import List, Optional
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        cursor = self._connection.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_name TEXT NOT NULL, 
        last_name TEXT NOT NULL) 
""")
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT id, first_name, last_name "
                       f"FROM {self.table_name}")
        rows = cursor.fetchall()
        actors = []
        for row in rows:
            actors.append(Actor(row[0], row[1], row[2]))
        return actors

    def get_by_id(self, actor_id: int) -> Optional[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name} WHERE id = ?",
            (actor_id,)
        )
        row = cursor.fetchone()
        if row:
            return Actor(row[0], row[1], row[2])
        return None

    def update(self, id: int,
               new_first_name: str,
               new_last_name: str) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} "
                       f"WHERE id = ?", (pk,))
        self._connection.commit()


if __name__ == "__main__":
    actor_manager = ActorManager("cinema", "actors")
