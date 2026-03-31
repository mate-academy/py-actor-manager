import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)

    def all(self) -> list:
        actors_cursor = self.conn.execute(
            f"SELECT id, "
            f"first_name, "
            f"last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(f"INSERT INTO {self.table_name} "
                          f"(first_name, last_name) "
                          f"VALUES (?, ?)", (first_name, last_name))
        self.conn.commit()

    def update(self,
               pk: int,
               new_first_name: str,
               new_last_name: str
               ) -> None:
        self.conn.execute(f"UPDATE {self.table_name} "
                          f"SET first_name = ?, "
                          f"last_name = ? "
                          f"WHERE id = ?",
                          (new_first_name,
                           new_last_name,
                           pk)
                          )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.conn.execute(f"DELETE FROM {self.table_name} "
                          f"WHERE id = ?",
                          (pk,)
                          )
        self.conn.commit()


if __name__ == "__main__":
    manager = ActorManager("movies.sqlite", "actors")
    manager.create("JOHN", "PITT")
    print(manager.all())
