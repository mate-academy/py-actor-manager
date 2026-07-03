import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        try:
            sql = (f"INSERT INTO {self.table_name} (first_name, last_name) "
                   f"VALUES(?, ?)")
            self.cursor.execute(sql, (first_name, last_name))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error: ", e)

    def all(self) -> list[Actor]:
        sql = f"SELECT * FROM {self.table_name}"
        result = self.cursor.execute(sql)

        actors = [Actor(actor[0], actor[1], actor[2]) for actor in result]

        return actors

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        sql = (f"UPDATE {self.table_name} SET first_name = ?, last_name = ?"
               f" WHERE id = ?")

        try:
            self.cursor.execute(sql, (new_first_name, new_last_name, pk))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error: ", e)

    def delete(
            self,
            pk: int
    ) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        try:
            self.cursor.execute(sql, (pk,))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error: ", e)
