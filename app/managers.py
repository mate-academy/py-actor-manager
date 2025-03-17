# managers.py
import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self, db_path: str = "cinema.db") -> None:
        """Инициализация менеджера с подключением к базе данных."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """Создание таблицы actors, если она не существует."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        """Создание нового актера в базе данных."""
        self.cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self.conn.commit()
        actor_id = self.cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        """Получение всех актеров из базы данных."""
        self.cursor.execute("SELECT id, first_name, last_name FROM actors")
        actors = []
        for row in self.cursor.fetchall():
            actor = Actor(id=row[0], first_name=row[1], last_name=row[2])
            actors.append(actor)
        return actors

    def update(self, actor_id: int, first_name: str, last_name: str) -> Actor:
        """Обновление данных актера по его id."""
        self.cursor.execute("""
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (first_name, last_name, actor_id))
        self.conn.commit()
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def delete(self, actor_id: int) -> None:
        """Удаление актера по его id."""
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()

    def __del__(self) -> None:
        """Закрытие соединения с базой данных при удалении объекта."""
        self.conn.close()
