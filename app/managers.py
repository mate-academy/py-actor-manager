import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

        # Создаём таблицу, если её нет
        sql = (
            "CREATE TABLE IF NOT EXISTS " + self.table_name + " ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL"
            ")"
        )
        self.cursor.execute(sql)
        self.connection.commit()

    # CREATE
    def create(self, first_name: str, last_name: str):
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    # READ ALL
    def all(self) -> list[Actor]:
        cursor = self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        return [Actor(*row) for row in rows]  # превращаем в список Actor

    # UPDATE
    def update(self, pk: int, new_first_name: str, new_last_name: str):
        self.cursor.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    # DELETE
    def delete(self, pk: int):
        self.cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (pk,)
        )
        self.connection.commit()

    # Закрыть соединение
    def close(self):
        self.connection.close()
