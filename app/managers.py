import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()
        create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} "
        create_table += "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
        create_table += "first_name TEXT, "
        create_table += "last_name TEXT)"

        self.cursor.execute(create_table)

    def create(self, first_name: str, last_name: str) -> None:
        query = f"INSERT INTO {self.table_name} (first_name, last_name) "
        query += "VALUES (?, ?);"
        # escreve dados dentro da tabela
        self.cursor.execute(query, (first_name, last_name))
        # grava dados no banco de dados
        self.connector.commit()

    def all(self) -> list:
        query = "SELECT *"
        query += f"FROM {self.table_name}"
        self.cursor.execute(query)
        # pega os dados salvos
        dados = self.cursor.fetchall()
        actor_list = []
        if dados:
            for info in dados:
                actor = Actor(
                    id=info[0],
                    first_name=info[1],
                    last_name=info[2])
                actor_list.append(actor)
        return actor_list

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        query = f"UPDATE {self.table_name} "
        query += "SET first_name = ?, last_name = ? "
        query += "WHERE id = ?"

        self.cursor.execute(query, (new_first_name, new_last_name, pk))
        self.connector.commit()

    def delete(self, pk: int) -> None:
        query = f"DELETE FROM {self.table_name} "
        query += "WHERE id = ?"
        self.cursor.execute(query, (pk,))
        self.connector.commit()
