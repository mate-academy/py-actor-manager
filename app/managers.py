import sqlite3
from typing import List, Optional
from app.models import Actor


class ActorManager:
    """Gerencia operações CRUD para atores em um banco SQLite."""

    def __init__(self, db_name: str, table_name: str) -> None:
        # Garante a regra do checklist: o nome da tabela sempre será plural
        if not table_name.endswith("s"):
            table_name += "s"

        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        """Cria a tabela de atores caso não exista."""
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str) -> Actor:
        """Cria um novo ator e retorna o objeto Actor correspondente."""
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self.table_name} "
                "(first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )
            actor_id = cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> List[Actor]:
        """Retorna todos os atores cadastrados."""
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT id, first_name, last_name FROM {self.table_name}"
            )
            rows = cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(
        self, pk: int, new_first_name: str, new_last_name: str
    ) -> Optional[Actor]:
        """Atualiza os dados de um ator pelo ID.

        Retorna o objeto atualizado.
        """
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (new_first_name, new_last_name, pk),
            )
            if cursor.rowcount == 0:
                return None
        return Actor(id=pk, first_name=new_first_name, last_name=new_last_name)

    def delete(self, pk: int) -> bool:
        """Remove um ator pelo ID.

        Retorna True se foi removido, False caso contrário.
        """
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?", (pk,)
            )
            return cursor.rowcount > 0
