import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.__create_table_if_not_exists()

    def __create_table_if_not_exists(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            f"first_name TEXT NOT NULL,last_name TEXT NOT NULL);"
        )
        self.conn.commit()
        cursor.close()

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        actor_id = cursor.lastrowid
        cursor.close()
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        cursor = self.conn.cursor()
        rows = cursor.execute(f"SELECT * FROM {self.table_name}").fetchall()
        cursor.close()
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2])
                for row in rows]

    def update(self,
               pk: int,
               new_first_name : str,
               new_last_name: str) -> Actor:
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE {self.table_name} "
                       f"SET first_name=?, last_name=? WHERE id=?",
                       (new_first_name, new_last_name, pk))
        self.conn.commit()
        row = cursor.execute(f"SELECT * FROM {self.table_name}"
                             f" WHERE id=?", (pk,)).fetchone()
        cursor.close()
        if row is None:
            raise Exception(f"Actor with id={pk} not found")
        return Actor(id=row[0], first_name=row[1], last_name=row[2])

    def delete(self, pk: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (pk,))
        self.conn.commit()
        cursor.close()

    def close(self) -> None:
        if self.conn:
            self.conn.close()
