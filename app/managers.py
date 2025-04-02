import sqlite3

class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS actors
                             (id INTEGER PRIMARY KEY,
                              first_name TEXT,
                              last_name TEXT)''')
        self.conn.commit()

    def create(self, first_name, last_name):
        self.conn.execute('INSERT INTO actors (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        self.conn.commit()

    def all(self):
        cursor = self.conn.execute('SELECT * FROM actors')
        return [Actor(*row) for row in cursor]

    def update(self, actor_id, first_name, last_name):
        self.conn.execute('UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?', (first_name, last_name, actor_id))
        self.conn.commit()

    def delete(self, actor_id):
        self.conn.execute('DELETE FROM actors WHERE id = ?', (actor_id,))
        self.conn.commit()
