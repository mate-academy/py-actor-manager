import sqlite3  # Usado para conexão direta com o banco SQLite

# Se quiser, importe o Actor do models para usar no tipo de retorno
from app.models import Actor

class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.connection.cursor()
        sql = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)"
        )
        cursor.execute(sql, (first_name, last_name))
        self.connection.commit()
        cursor.close()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM {self.table_name}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()

        actors = []
        for row in rows:
            actor = Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            actors.append(actor)
        return actors

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        cursor = self.connection.cursor()
        sql = (
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ?"
        )
        cursor.execute(sql, (new_first_name, new_last_name, pk))
        self.connection.commit()
        cursor.close()

    def delete(self, pk: int) -> None:
        cursor = self.connection.cursor()
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        cursor.execute(sql, (pk,))
        self.connection.commit()
        cursor.close()
