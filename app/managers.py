import sqlite3
from typing import List
from models import Actor

class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        # Establecemos la conexión y el cursor globales para la instancia
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        
        # Opcional pero recomendado: Asegurar que la tabla exista con la estructura correcta
        self._ensure_table_exists()

    def _ensure_table_exists(self):
        """Crea la tabla si no existe para evitar errores en las operaciones CRUD."""
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        """Crea una nueva entrada en la tabla con las propiedades dadas."""
        query = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?);"
        self.cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> List[Actor]:
        """Devuelve una lista de instancias de Actor desde la DB."""
        query = f"SELECT id, first_name, last_name FROM {self.table_name};"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        # Mapeamos cada fila tupla a una instancia de la dataclass Actor
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        """Actualiza las propiedades de la entrada con el pk dado."""
        query = f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?;"
        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connection.commit()

    def delete(self, pk: int) -> None:
        """Elimina la entrada con el pk dado de la DB."""
        query = f"DELETE FROM {self.table_name} WHERE id = ?;"
        self.cursor.execute(query, (pk,))
        self.connection.commit()

    def __del__(self):
        """Asegura el cierre de la conexión cuando el manager se destruye."""
        if hasattr(self, 'connection'):
            self.connection.close()
