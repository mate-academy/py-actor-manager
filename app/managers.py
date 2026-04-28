import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        query = f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> None:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.connection.cursor()
        data = cursor.execute(query)
        return [Actor(*item) for item in data]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? "
                 f"WHERE id = ?")
        cursor = self.connection.cursor()
        cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        query = (f"DELETE FROM {self.table_name} "
                 f"WHERE id = ?")
        cursor = self.connection.cursor()
        cursor.execute(query, (pk, ))
        self.connection.commit()
