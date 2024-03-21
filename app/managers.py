import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        sql = (f"INSERT INTO {self.table_name} "
               f"(first_name, last_name) VALUES (?, ?)")
        self.conn.execute(sql, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list:
        sql = f"SELECT * FROM {self.table_name}"
        actor_cursor = self.conn.execute(sql)
        return [Actor(*row) for row in actor_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        updates = []
        params = []
        if first_name:
            updates.append("first_name = ?")
            params.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            params.append(last_name)
        params.append(actor_id)
        sql = f"UPDATE {self.table_name} SET {', '.join(updates)} WHERE id = ?"
        self.conn.execute(sql, tuple(params))
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.conn.execute(sql, (actor_id,))
        self.conn.commit()
