import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def all(self):
        actor_manager_coursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return[Actor(*row) for row in actor_manager_coursor]

    def create(self,first_name:str, last_name: str ):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
                "VALUES (?, ?) ",
            (first_name, last_name,)
             )
        self._connection.commit()

    def update(self, pk, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
                "SET first_name = ?, "
                "last_name = ? "
                "WHERE id = ? ",
            (new_first_name, new_last_name, pk)
            )

    def delete(self, pk):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (pk,)                     )