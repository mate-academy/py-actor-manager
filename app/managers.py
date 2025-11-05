import sqlite3
from typing import List, Optional

from app.models import Actor


class ActorManager(object):
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        query = ("CREATE TABLE IF NOT EXISTS {} "
                 "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "first_name TEXT NOT NULL,"
                 "last_name TEXT NOT NULL)"
                 ).format(self.table_name)
        self.cursor.execute(query)
        self.conn.commit()

    def all(self) -> List[Actor]:
        query = ("SELECT id, first_name, last_name"
                 " FROM {} "
                 "ORDER BY id"
                 ).format(self.table_name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if not rows:
            return []

        actors_list = [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]
        return actors_list

    def create(self, first_name: str, last_name: str) -> Optional[Actor]:
        query = ("INSERT INTO {} (first_name, last_name) "
                 "VALUES (?, ?)"
                 ).format(self.table_name)
        try:
            self.cursor.execute(query, (first_name, last_name))
            self.conn.commit()
            new_id = self.cursor.lastrowid

            return Actor(id=new_id, first_name=first_name, last_name=last_name)
        except sqlite3.Error as error:
            raise error

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> Optional[Actor]:
        query = ("UPDATE {} "
                 "SET first_name=?, last_name=?"
                 " WHERE id=?"
                 ).format(self.table_name)
        try:
            self.cursor.execute(query, (new_first_name, new_last_name, pk))
            self.conn.commit()
        except sqlite3.Error as error:
            self.conn.rollback()
            raise error

        if self.cursor.rowcount == 0:
            return None
        else:
            return Actor(
                id=pk,
                first_name=new_first_name,
                last_name=new_last_name
            )

    def delete(self, pk: int) -> None:
        query = ("DELETE FROM {} WHERE id=?").format(self.table_name)
        self.cursor.execute(query, (pk,))
        self.conn.commit()
