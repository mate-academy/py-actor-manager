import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        # Створюємо підключення до БД (Connection)
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        # Створюємо курсор для виконання SQL-запитів
        cursor = self.connection.cursor()

        # Використовуємо f-строку ЛИШЕ для назви таблиці,
        # а значення передаємо через ? для безпеки від SQL-ін'єкцій
        query = (
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)"
        )
        cursor.execute(query, (first_name, last_name))

        # Обов'язково зберігаємо зміни в базі
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.cursor()
        query = (
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        cursor.execute(query)

        # Отримуємо всі рядки з бази
        rows = cursor.fetchall()

        # Перетворюємо кожен рядок (кортеж) на об'єкт нашого датакласу Actor
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cursor = self.connection.cursor()
        query = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?"
        )
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        cursor = self.connection.cursor()
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        cursor.execute(query, (pk,))
        self.connection.commit()
