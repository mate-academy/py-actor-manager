import sqlite3
import os.path

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.db_name = os.path.join("..", "cinema.db")
        self.table_name = "actors"
        self._connection = sqlite3.connect(
            self.db_name
        )

    def all(self) -> list[Actor]:
        select_all_sql = f"""
                        SELECT * FROM {self.table_name}
                        """
        cinema_actors_cursor = self._connection.execute(
            select_all_sql
        )
        return [
            Actor(*row) for row in cinema_actors_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        insert_sql = f"""
                    INSERT INTO {self.table_name}
                    (first_name, last_name)
                    VALUES(?, ?)
                    """
        self._connection.execute(
            insert_sql,
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
            self,
            updated_id: int,
            updated_first_name: str,
            updated_last_name: str
    ) -> None:
        update_sql = f"""
                    UPDATE {self.table_name}
                    SET first_name = ?, last_name = ?
                    WHERE id = ?
                    """
        self._connection.execute(
            update_sql,
            (updated_first_name, updated_last_name, updated_id)
        )
        self._connection.commit()

    def delete(self, deleted_id: int) -> None:
        deleted_sql = f"""
                    DELETE FROM {self.table_name}
                    WHERE id = ?
                    """
        self._connection.execute(
            deleted_sql,
            (deleted_id,)
        )
        self._connection.commit()
