import sqlite3
from string import Template
from app.models import Actor


class ActorManager:
    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        query = Template(
            "INSERT INTO $table (first_name, last_name) VALUES (?, ?)"
        )
        self._connection.execute(
            query.substitute(table=self.table_name),
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        query = Template("SELECT * FROM $table")
        actor_table_list = self._connection.execute(
            query.substitute(table=self.table_name)
        )
        return [
            Actor(*row) for row in actor_table_list
        ]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        query = Template(
            "UPDATE $table SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self._connection.execute(
            query.substitute(table=self.table_name),
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        query = Template("DELETE FROM $table WHERE id = ?")
        self._connection.execute(
            query.substitute(table=self.table_name),
            (pk,)
        )
        self._connection.commit()
