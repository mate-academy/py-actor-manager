import sqlite3
from sqlite3 import Connection


from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name: str = db_name
        self.table_name: str = table_name
        self.connection: Connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        query: str = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        query: str = f"""
        INSERT INTO {self.table_name} (first_name, last_name)
        VALUES (?, ?);
        """
        result = self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

        actor_id: int = result.lastrowid

        return Actor(
            id=actor_id,
            first_name=first_name,
            last_name=last_name,
        )

    def all(self) -> list[Actor]:
        query: str = f"""
        SELECT id, first_name, last_name
        FROM {self.table_name};
        """
        rows = self.connection.execute(query).fetchall()

        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for row in rows
        ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        query: str = f"""
        UPDATE {self.table_name}
        SET first_name = ?, last_name = ?
        WHERE id = ?;
        """
        self.connection.execute(
            query,
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query: str = f"""
        DELETE FROM {self.table_name}
        WHERE id = ?;
        """
        self.connection.execute(query, (pk,))
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
