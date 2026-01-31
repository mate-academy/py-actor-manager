import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.con = sqlite3.connect(db_name)

    def create(self, first_name: str, last_name: str) -> None:
        cur = self.con.cursor()
        cur.execute(
            f"INSERT INTO {self.table_name}"
            f"(first_name, last_name) VALUES (?, ?)", (first_name, last_name)
        )
        self.con.commit()
        cur.close()

    def all(self) -> list:
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM {self.table_name}")
        rows = cur.fetchall()
        cur.close()

        actors_list = []
        for row in rows:
            actor = Actor(row[0], row[1], row[2])
            actors_list.append(actor)
        return actors_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        cur = self.con.cursor()
        cur.execute(f"UPDATE {self.table_name} SET first_name=?, last_name=?"
                    f"WHERE id=?", (new_first_name, new_last_name, pk,))
        self.con.commit()
        cur.close()

    def delete(self, pk: int) -> None:
        cur = self.con.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id=?", (pk,))
        self.con.commit()
        cur.close()
