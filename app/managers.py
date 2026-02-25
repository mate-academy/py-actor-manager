import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(db_name)

