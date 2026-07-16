import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    # A __init__ metódus mindig None-t ad vissza
    def __init__(self, db_name: str, table_name: str) -> None:
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    # A create metódus is None-t ad vissza
    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    # Itt egy listát adunk vissza, amiben Actor objektumok vannak
    def all(self) -> list[Actor]:
        query = f"SELECT id, first_name, last_name FROM {self.table_name}"
        cursor = self.connection.execute(query)
        return [Actor(id=row[0], first_name=row[1],
                      last_name=row[2]) for row in cursor.fetchall()]

    # Az update metódus is None-t ad vissza
    def update(self, pk: int, new_first_name: str, new_last_name: str)\
            -> None:
        query = (f"UPDATE {self.table_name} "
                 f"SET first_name = ?, last_name = ? WHERE id = ?")
        self.connection.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    # A delete metódus is None-t ad vissza
    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(query, (pk,))
        self.connection.commit()
