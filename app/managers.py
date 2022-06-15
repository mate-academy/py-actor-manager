import sqlite3

from models import Actor


class ActorManager:

    def __init__(self):
        self._connection = sqlite3.connect('cinema.db3')
        self.name_table = 'actors'

    def create(self, first_name, last_name):
        self._connection.execute(f"INSERT INTO {self.name_table}"
                                 "(first_name, last_name) "
                                 "VALUES (?, ?)",
                                 (first_name, last_name))
        self._connection.commit()

    def all(self):
        cursor = self._connection.execute(f"SELECT * FROM {self.name_table}")

        return [Actor(*row) for row in cursor]

    def update(self, id_to_update: int,
               new_first_name: str,
               new_last_name: str
               ):
        self._connection.execute(f"UPDATE {self.name_table} "
                                 "SET first_name = ?, last_name = ? "
                                 "WHERE id = ?", (new_first_name,
                                                  new_last_name,
                                                  id_to_update))
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(f"DELETE FROM {self.name_table} "
                                 "WHERE id = ?", (id_to_delete,))

        self._connection.commit()
