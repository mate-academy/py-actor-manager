import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        cur = self.conn.cursor()
        create_table = (f"CREATE TABLE IF "
                        f"NOT EXISTS {self.table_name} (id "
                        f"INTEGER PRIMARY KEY "
                        f"AUTOINCREMENT, first_name TEXT, "
                        f"last_name TEXT)"
                        )
        cur.execute(create_table)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        cur = self.conn.cursor()
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)"
                 )
        cur.execute(query, (first_name, last_name))
        self.conn.commit()
        new_id = cur.lastrowid
        return Actor(first_name=first_name, last_name=last_name, id=new_id)

    def all(self) -> list[Actor]:
        cur = self.conn.cursor()
        query = (f"SELECT * FROM {self.table_name}")
        cur.execute(query)
        rows = cur.fetchall()
        actors = [Actor(id=row[0],
                        first_name=row[1],
                        last_name=row[2]) for row in rows
                  ]
        return actors

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        cur = self.conn.cursor()
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? WHERE id = ?")
        cur.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()
        return cur.rowcount > 0

    def delete(self, pk: int) -> bool:
        cur = self.conn.cursor()
        query = (f"DELETE FROM {self.table_name} WHERE id = ?")
        cur.execute(query, (pk,))
        self.conn.commit()
        return cur.rowcount > 0

    def close(self) -> None:
        self.conn.close()
