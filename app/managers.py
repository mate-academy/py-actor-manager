import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("../actors_db.sqlite")
        self.table_name = "actors"

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        print(f"Actors_cursor: {actors_cursor}")
        for row in actors_cursor:
            print(row)

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
        (new_first_name, new_last_name, id_to_update),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
    manager.create("Courtney", "Miller")
    manager.all()
    manager.update(3, "Courtney", "Topp")
    manager.all()
    manager.delete(3)
    manager.all()