import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name}'
                         f'(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)')

    def create(self, first_name: str, last_name: str) -> None:
        self.cur.execute(f'INSERT INTO {self.table_name}'
                         f'(first_name, last_name) VALUES '
                         f'(?, ?)', (first_name, last_name))
        self.con.commit()

    def all(self) -> list[Actor]:
        actors = self.cur.execute(f'SELECT * FROM '
                                  f'{self.table_name}').fetchall()
        result = []
        if len(actors) == 0:
            return result

        for actor in actors:
            result.append(Actor(id=actor[0],
                                first_name=actor[1], last_name=actor[2]))
        return result

    def update(self, pk: int, new_first_name: str,
               new_last_name: str) -> None:
        self.cur.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.con.commit()

    def delete(self, pk: int) -> None:
        self.cur.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.con.commit()
