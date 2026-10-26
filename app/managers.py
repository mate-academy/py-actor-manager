import sqlite3

from app.models import Actor

class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL                        
            )
                            
        """)

        self.connect.commit()

    def create(self, first_name, last_name):
        self.cursor.execute(f"""
                INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)
            """, (first_name, last_name))

        self.connect.commit()

        actor_id = self.cursor.lastrowid

        return Actor(
            id = actor_id,
            first_name = first_name,
            last_name = last_name
        )
    
    def all(self):
        self.cursor.execute(f"""
            SELECT * FROM {self.table_name}
            ORDER BY id
        """)
        rows = self.cursor.fetchall()
    
        actors = []

        for row in rows:
            actor = Actor(
                id = row[0],
                first_name=row[1], 
                last_name=row[2]
            )

            actors.append(actor)
            
        return actors
    
    def update(self, pk, new_first_name, new_last_name):
        self.cursor.execute(f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (new_first_name, new_last_name, pk))

        self.connect.commit()

    def delete(self, pk):
        self.cursor.execute(f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
        """, (pk,))

        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()