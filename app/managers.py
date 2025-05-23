from pathlib import Path
import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        assert table_name.isidentifier(), "Invalid table name"

        self.db_name = db_name
        self.table_name = table_name

        base_dir = Path(__file__).resolve().parent
        db_path = base_dir / "database" / db_name

        db_path.parent.mkdir(parents=True, exist_ok=True)

        self._connection = sqlite3.connect(str(db_path))
        self._cursor = self._connection.cursor()

        sql = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL"
            ")"
        )
        self._cursor.execute(sql)
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._cursor.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        rows = self._cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in rows]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        self._cursor.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (pk,)
        )
        self._connection.commit()
