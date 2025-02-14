import sqlite3
from typing import List, Optional, Union

from models import Actor


class ActorManager:
    def __init__(self, db_path: str = "cinema.db") -> None:
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def _get_connection(self) -> sqlite3.Connection:
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def create_table(self) -> None:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS actors (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Помилка при створенні таблиці: {e}")

    def create(self, first_name: str, last_name: str) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO actors (first_name, last_name)
                    VALUES (?, ?)
                """, (first_name, last_name))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Помилка при створенні актора: {e}")
            return None

    def get(self, actor_id: int) -> Optional[Actor]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, first_name, last_name
                    FROM actors
                    WHERE id = ?
                """, (actor_id,))
                row = cursor.fetchone()
                if row:
                    return Actor(id=row["id"], first_name=row["first_name"],
                                 last_name=row["last_name"])
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Помилка при отриманні актора: {e}")
            return None

    def all(self) -> List[Actor]:
        actors: List[Actor] = []
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, first_name, last_name
                    FROM actors
                """)
                rows = cursor.fetchall()
                for row in rows:
                    actors.append(Actor(id=row["id"],
                                        first_name=row["first_name"],
                                        last_name=row["last_name"]))
        except sqlite3.Error as e:
            print(f"Помилка при отриманні всіх акторів: {e}")
        return actors

    def update(self, actor_id: int, first_name: Optional[str] = None,
               last_name: Optional[str] = None) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                update_fields = []
                params: List[Union[str, int]] = []
                if first_name is not None:
                    update_fields.append("first_name = ?")
                    params.append(first_name)
                if last_name is not None:
                    update_fields.append("last_name = ?")
                    params.append(last_name)

                if not update_fields:
                    return True

                sql = f"""
                    UPDATE actors
                    SET {", ".join(update_fields)}
                    WHERE id = ?
                """
                params.append(actor_id)
                cursor.execute(sql, params)
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Помилка при оновленні актора: {e}")
            return False

    def delete(self, actor_id: int) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM actors
                    WHERE id = ?
                """, (actor_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Помилка при видаленні актора: {e}")
            return False

    def close(self) -> None:
        if self.conn:
            self.conn.close()
            self.conn = None
