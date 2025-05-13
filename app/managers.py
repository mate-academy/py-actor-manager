import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        is_table = self.cur.execute(
            f"SELECT name FROM sqlite_master "
            f"WHERE name = '{self.table_name}'"
        )
        if is_table.fetchone() is None:
            self.cur.execute(
                f"CREATE TABLE {self.table_name}("
                "pk INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)"
            )

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cur.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        pk = self.cur.lastrowid
        inserted_actor = self.cur.execute(f"SELECT * FROM"
                                          f" {self.table_name} WHERE id = ? "
                                          , (pk,)).fetchone()
        return Actor(inserted_actor[0], inserted_actor[1], inserted_actor[2])

    def all(self) -> list[tuple]:
        actors = self.cur.execute(
            f"SELECT * FROM {self.table_name}"
        ).fetchall()
        result = []
        if len(actors) == 0:
            return result
        for i in actors:
            result.append(Actor(i[0], i[1], i[2]))
        return result

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (pk,)
        )
        self.conn.commit()
