import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self,
                 db_name: str,
                 table_name: str
                 ) -> None:
        self.db_name = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cur = self.db_name.cursor()
        cur.execute(f"INSERT INTO {self.table_name} "
                    f"({first_name} {last_name})")
        self.db_name.commit()

    def all(self) -> List[Actor]:
        all_content = self.db_name.execute(f"SELECT * FROM"
                                           f" {self.table_name}").fetchall()
        return [Actor(*raw) for raw in all_content]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cur = self.db_name.cursor()
        cur.execute(f"UPDATE {self.table_name} SET"
                    f" {new_first_name} {new_last_name} WHERE {pk}")
        self.db_name.commit()

    def delete(self, pk: int) -> None:
        cur = self.db_name.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE {pk}")
        cur.close()
