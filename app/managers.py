import sqlite3

from app.models import Actor


class ActorManager():
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"""
                INSERT INTO {self.table_name}
                (first_name, last_name) VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        actor_list = []
        actor_db_list = self.connection.execute(
            f"""
                SELECT id, first_name, last_name
                FROM {self.table_name}
            """
        )
        for actor in actor_db_list:
            actor_list.append(Actor(*actor))
        return actor_list

    def update(
            self, pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.connection.execute(
            f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """,
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        self.connection.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (pk,)
        )
        self.connection.commit()
