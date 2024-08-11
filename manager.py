import sqlite3

from model import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect('../cinema.sqlite')
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def all(self):
        actor_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor.fetchall()]

    def update(self, id_to_update, new_first_name: str, new_last_name: str):
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (id_to_update, new_first_name, new_last_name,)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int):
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=? ",
            (id_to_delete,)
        )
        self.connection.commit()


if __name__ == '__main__':
    Actor.objects = ActorManager()
    print(Actor.objects.all())
