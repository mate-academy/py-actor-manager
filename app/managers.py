import sqlite3


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actor"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}",
        )
        return [row for row in actor_cursor]

    def update(self, id_to_update, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?", (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
