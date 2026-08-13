import sqlite3


from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> None:
        cur = self.conn.cursor()
        query = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cur.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        cur = self.conn.cursor()
        cur.execute(f"SELECT id, first_name, last_name FROM {self.table_name}")
        rows = cur.fetchall()
        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cur = self.conn.cursor()
        query = (
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        cur.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.conn.commit()
