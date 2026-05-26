import sqlite3


from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str = "actors") -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)
        self.cursor = self._connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} "
                            f"( id INTEGER PRIMARY KEY, "
                            f"first_name TEXT NOT NULL, "
                            f"last_name TEXT NOT NULL ) ")
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f"INSERT INTO {self.table_name} "
                             f"(first_name, last_name) VALUES (?, ?)",
                             (first_name, last_name)
                             )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = actor_cursor.fetchall()
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f"UPDATE {self.table_name} "
                             f"SET first_name = ?, last_name = ? "
                             f"WHERE id = ?",
                             (new_first_name, new_last_name, pk))
        self._connection.commit()

    def delete(self, pk: int) -> None:
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f"DELETE FROM {self.table_name} "
                             f"WHERE id = ?", (pk, )
                             )
        self._connection.commit()
