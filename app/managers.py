import sqlite3


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

    def update(self, id_to_upd: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_upd)
        )
        self._connection.commit()

    def delete(self, id_to_del):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_del, )
        )
        self._connection.commit()
