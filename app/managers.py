import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(f"""
                            INSERT INTO {self.table_name} 
                            (first_name, last_name) VALUES (?, ?)
                            """, (first_name, last_name))
        self.connect.commit()

    def all(self) -> list:
        tuples = self.cursor.execute(f"""
                                     SELECT * FROM {self.table_name}
                                     """).fetchall()
        all_actors = [Actor(*t) for t in tuples]

        return all_actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(f"""
                            UPDATE {self.table_name} 
                            SET first_name = ?, last_name = ? WHERE id = ?
                            """, (new_first_name, new_last_name, pk))
        self.connect.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(f"""
                            DELETE FROM {self.table_name} 
                            WHERE id = ?
                            """, (pk,))
        self.connect.commit()
