import sqlite3

class ActorManager:
    def __init__(self, conn):
        """Принимаем объект соединения с базой данных"""
        if isinstance(conn, sqlite3.Connection):
            self.conn = conn
        else:
            raise TypeError("Expected sqlite3.Connection object")

        self.cursor = self.conn.cursor()

    def create(self, first_name, last_name):
        """Создаёт нового актёра и возвращает его id"""
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self):
        """Возвращает список всех актёров"""
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [{"id": row[0], "first_name": row[1], "last_name": row[2]} for row in rows]

    def update(self, actor_id, first_name, last_name):
        """Обновляет данные актёра по id"""
        self.cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self.conn.commit()

    def delete(self, actor_id):
        """Удаляет актёра по id"""
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()