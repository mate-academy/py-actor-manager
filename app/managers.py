import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()
        self.id_count = 1

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL)
        """)
        self.connect.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(f"""
        INSERT INTO {self.table_name} VALUES ({self.id_count}, '{first_name}', '{last_name}')
        """)
        self.connect.commit()
        self.id_count += 1

    def all(self) -> list:
        tuples = self.cursor.execute(f"""
                                     SELECT * FROM {self.table_name}
                                     """).fetchall()
        all_actors = []

        for tuple in tuples:
            all_actors.append(Actor(*tuple))

        return all_actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(f"""
                            UPDATE {self.table_name} SET first_name = '{new_first_name}', last_name = '{new_last_name}' WHERE id = {pk}
                            """)
        self.connect.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(f"""
                            DELETE FROM {self.table_name} WHERE id = {pk} 
                            """)
        self.connect.commit()
