# =========================
# File: app/managers.py
# =========================
import sqlite3
from typing import List, Optional
from contextlib import contextmanager

# Importação correta da classe Actor de models.py
from app.models import Actor


class ActorManager:
    """Gerenciador CRUD para a tabela de atores em um banco SQLite."""

    def __init__(self, db_name: str, table_name: str = "actors"):
        """
        Inicializa o gerenciador com conexão ao banco de dados.
        
        Args:
            db_name: Nome do arquivo do banco de dados
            table_name: Nome da tabela (padrão: "actors")
        """
        self.db_name = db_name
        self.table_name = table_name
        
        # Validação básica do nome da tabela
        if not table_name.replace("_", "").isalnum():
            raise ValueError("Nome da tabela deve conter apenas letras, números e underscores")
        
        # Cria conexão
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
        
        # Cria a tabela se não existir
        self._create_table()
    
    @contextmanager
    def _get_cursor(self):
        """Context manager para obter e fechar cursor automaticamente."""
        cursor = self.conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
    
    def _create_table(self) -> None:
        """Cria a tabela de atores se não existir."""
        with self._get_cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
            """)
            self.conn.commit()
    
    def create(self, first_name: str, last_name: str) -> Actor:
        """
        Cria um novo ator no banco de dados.
        
        Args:
            first_name: Primeiro nome do ator
            last_name: Sobrenome do ator
            
        Returns:
            Instância de Actor com o ID gerado
        """
        with self._get_cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )
            self.conn.commit()
            
            # Recupera o ID gerado
            actor_id = cursor.lastrowid
            
            if actor_id is None:
                # Para bancos que não suportam lastrowid, faz uma consulta
                cursor.execute(f"SELECT last_insert_rowid() as id")
                actor_id = cursor.fetchone()["id"]
            
            return Actor(id=actor_id, first_name=first_name, last_name=last_name)
    
    def all(self) -> List[Actor]:
        """
        Retorna todos os atores do banco de dados.
        
        Returns:
            Lista de instâncias de Actor
        """
        with self._get_cursor() as cursor:
            cursor.execute(f"SELECT id, first_name, last_name FROM {self.table_name}")
            rows = cursor.fetchall()
            
            return [
                Actor(
                    id=row["id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"]
                )
                for row in rows
            ]
    
    def update(self, pk: int, new_first_name: str, new_last_name: str) -> bool:
        """
        Atualiza os dados de um ator.
        
        Args:
            pk: ID do ator a ser atualizado
            new_first_name: Novo primeiro nome
            new_last_name: Novo sobrenome
            
        Returns:
            True se o ator foi atualizado, False caso contrário
        """
        with self._get_cursor() as cursor:
            cursor.execute(
                f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
                (new_first_name, new_last_name, pk)
            )
            self.conn.commit()
            
            # Retorna True se alguma linha foi afetada
            return cursor.rowcount > 0
    
    def delete(self, pk: int) -> bool:
        """
        Exclui um ator do banco de dados.
        
        Args:
            pk: ID do ator a ser excluído
            
        Returns:
            True se o ator foi excluído, False caso contrário
        """
        with self._get_cursor() as cursor:
            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (pk,)
            )
            self.conn.commit()
            
            # Retorna True se alguma linha foi afetada
            return cursor.rowcount > 0
    
    def get(self, pk: int) -> Optional[Actor]:
        """
        Obtém um ator específico pelo ID.
        
        Args:
            pk: ID do ator
            
        Returns:
            Instância de Actor ou None se não encontrado
        """
        with self._get_cursor() as cursor:
            cursor.execute(
                f"SELECT id, first_name, last_name FROM {self.table_name} WHERE id = ?",
                (pk,)
            )
            row = cursor.fetchone()
            
            if row:
                return Actor(
                    id=row["id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"]
                )
            return None
    
    def close(self) -> None:
        """Fecha a conexão com o banco de dados."""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
    
    def __enter__(self):
        """Suporte para context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fecha a conexão ao sair do context manager."""
        self.close()
    
    def __del__(self):
        """Fecha a conexão quando o objeto é destruído."""
        try:
            self.close()
        except:
            pass
