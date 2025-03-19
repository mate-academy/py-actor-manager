import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self.conn.commit()

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        if first_name:
            self.cursor.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ? WHERE id = ?", (first_name, actor_id)
            )
        if last_name:
            self.cursor.execute(
                f"UPDATE {self.table_name} "
                f"SET last_name = ? WHERE id = ?", (last_name, actor_id)
            )
        self.conn.commit()

    def all(self) -> List[Actor]:
        actors = (self.cursor.execute(f"SELECT * "
                                      f"FROM {self.table_name}").fetchall())
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2])
                for row in actors]

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (actor_id,)
        )
        self.conn.commit()

    def close_connection(self) -> None:
        self.conn.close()
