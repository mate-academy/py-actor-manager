import sqlite3
import models


class ActorManager:
    def __init__(self):
        self._table_name = "actors"
        self.manager = sqlite3.connect("cinema.db3")

    def create(self, first_name, last_name):
        self.manager.execute(f"INSERT INTO {self._table_name} "
                             f"(first_name, last_name) VALUES(?, ?)",
                             (first_name, last_name))
        self.manager.commit()

    def update(self, id_to_update, new_first_name, new_last_name):
        self.manager.execute(f"UPDATE {self._table_name} "
                             f"SET first_name = ?, last_name = ? "
                             f"WHERE id = ?",
                             (new_first_name, new_last_name, id_to_update))
        self.manager.commit()

    def delete(self, id_to_delete):
        self.manager.execute(f"DELETE FROM {self._table_name} "
                             f"WHERE id = ?",
                             (id_to_delete, ))
        self.manager.commit()

    def all(self):
        manager_cursor = self.manager.execute(f"SELECT * "
                                              f"FROM {self._table_name}")
        return [models.Actor(*row) for row in manager_cursor]
