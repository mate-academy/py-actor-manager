import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        sql_query_part_1 = f"INSERT INTO {self.table_name} "
        sql_query_part_2 = "(first_name, last_name) VALUES (?, ?)"
        sql_query = sql_query_part_1 + sql_query_part_2

        self.cursor.execute(sql_query, (first_name, last_name))
        self.connect.commit()

    def all(self) -> list:
        sql_query = f"SELECT * FROM {self.table_name}"

        tuples = self.cursor.execute(sql_query).fetchall()
        all_actors = [Actor(*t) for t in tuples]

        return all_actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        sql_query_part_1 = f"UPDATE {self.table_name} "
        sql_query_part_2 = "SET first_name = ?, last_name = ? WHERE id = ?"
        sql_query = sql_query_part_1 + sql_query_part_2

        self.cursor.execute(sql_query, (new_first_name, new_last_name, pk))
        self.connect.commit()

    def delete(self, pk: int) -> None:
        sql_query = f"DELETE FROM {self.table_name} WHERE id = ?"

        self.cursor.execute(sql_query, (pk,))
        self.connect.commit()
