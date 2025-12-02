import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        """ Creates new row (Actor) in table. """
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        """ Returns a list of Actor class objects from table. """
        query = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        actor_list = []
        for row in rows:
            actor_list.append(Actor(row[0], row[1], row[2]))
        return actor_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """ Updates row (Actor) class object with new data. """
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? WHERE id = ?"
                 )
        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, pk: int) -> None:
        """ Deletes row (Actor) class object from table with given id. """
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (pk,))
        self.conn.commit()
