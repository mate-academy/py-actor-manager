from models import Actor
import sqlite3


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db")
        self.cur = self.connection.cursor()

    def create(self, first_name, last_name):

        self.cur.execute('SELECT COUNT(*) FROM actors')
        id = self.cur.fetchone()[0] + 1

        try:
            self.cur.execute(
                'INSERT INTO actors (id, first_name, last_name)\
                    VALUES (?, ?, ?)',
                (id, first_name, last_name)

            )
            self.connection.commit()

        except sqlite3.Error as e:
            print(f'Error {e} occured')

    def all(self):

        records = self.cur.execute('SELECT * FROM actors')
        actors = []

        for actor in records:
            actors.append(Actor(actor[0], actor[1], actor[2]))

        return actors

    def update(self, actor_id, first_name, last_name):

        sql = 'UPDATE actors SET \
                first_name = ?, last_name = ?\
                WHERE id = ?'
        val = (first_name, last_name, actor_id)

        try:
            self.cur.execute(sql, val)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f'Error {e} occured')

    
