import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("C:/Users/Asus/projects/my_project/py-actor-manager/py-actor-manager/cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name,)
        )
        self._connection.commit()


    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name  = ? ,last_name  = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self,id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()

    print("Усі актори:", manager.all())
