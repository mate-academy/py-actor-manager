import sqlite3
from app.models import Actor


class ActorManager:
    """
    Manages CRUD operations for Actor entries in a database.

    This class provides methods to create, read, update, and delete
    actor records in a SQLite database.

    Attributes:
        db_name (str): The name of the database file.
        table_name (str): The name of the table in the database.
        connection (sqlite3.Connection): The database connection object.
    """

    def __init__(self, db_name: str, table_name: str) -> None:
        """
        Initialize the ActorManager with database connection.

        Args:
            db_name (str): The name of the database file.
            table_name (str): The name of the table to manage.

        Raises:
            ValueError: If table_name contains invalid characters.
        """
        self.db_name = db_name
        self.table_name = self._validate_table_name(table_name)
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _validate_table_name(self, table_name: str) -> str:
        """
        Validate and sanitize the table name to prevent SQL injection.

        Args:
            table_name (str): The table name to validate.

        Returns:
            str: The validated table name.

        Raises:
            ValueError: If table_name contains invalid characters.
        """
        if not table_name.replace("_", "").isalnum():
            raise ValueError(
                "Table name must contain only alphanumeric "
                "characters and underscores"
            )
        return table_name

    def _create_table(self) -> None:
        """Create the actors table if it doesn"t exist.

        Creates a table with columns: id (PRIMARY KEY), first_name, last_name.
        """
        cursor = self.connection.cursor()
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}
        (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, last_name TEXT NOT NULL)
        """
        cursor.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        """Create a new actor entry in the database.

        Args:
            first_name (str): The actor"s first name.
            last_name (str): The actor"s last name.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        """Retrieve all actor entries from the database.

        Returns:
            list[Actor]: A list of Actor instances. Returns an empty list
                if there are no entries in the table.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        rows = cursor.fetchall()

        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """Update an actor"s properties by primary key.

        Args:
            pk (int): The primary key of the actor to update.
            new_first_name (str): The new first name for the actor.
            new_last_name (str): The new last name for the actor.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        """Delete an actor entry by primary key.

        Args:
            pk (int): The primary key of the actor to delete.
        """
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self.connection.commit()

    def __del__(self) -> None:
        """Close the database connection when the manager is destroyed."""
        if hasattr(self, "connection"):
            self.connection.close()
