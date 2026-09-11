import sqlite3
from app.models import Actor


class ActorManager:

    def __init__(
        self, db_name: str = "managers.db", table_name: str = "actors"
    ) -> None:
        self.conexao = sqlite3.connect(db_name)
        self.cursor = self.conexao.cursor()
        self.table_name = table_name
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS " + table_name + " ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name VARCHAR(50), "
            "last_name VARCHAR(50));"
        )
        self.conexao.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conexao.commit()

    def all(self) -> list:
        rows = self.cursor.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        ).fetchall()
        return [
            Actor(id=r[0], first_name=r[1], last_name=r[2])
            for r in rows
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.conexao.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.conexao.commit()
