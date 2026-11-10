import sqlite3


from app.models import Actor


class ActorManager:

    def __init__(self, db_name: str, table_name: str) -> None:
        self.db = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self.db.cursor()

        cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )

        self.db.commit()

    def all(self) -> list[Actor]:
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table_name} "
        )

        rows = cursor.fetchall()

        actors = []
        for row in rows:
            actor = Actor(*row)
            actors.append(actor)

        return actors

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str,
    ) -> None:
        cursor = self.db.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )

        self.db.commit()

    def delete(self, pk: int) -> None:
        cursor = self.db.cursor()
        cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (pk,)
        )
        self.db.commit()
