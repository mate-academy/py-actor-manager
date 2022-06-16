import sqlite3


from models import Actor


class ActorManager:
    def __init__(self):
        self.db = sqlite3.connect(r'cinema.sqlite')
        self.cursor = self.db.cursor()

    def create(self, first_name, last_name):
        create_string = f"INSERT INTO actor(first_name, last_name) " \
                        f"VALUES('{first_name}', '{last_name}')"
        self.cursor.execute(create_string)
        self.db.commit()

    def update(self, id_: int, first_name, last_name):
        update_string = "UPDATE actor " \
                        "SET first_name = ?, last_name = ?" \
                        " WHERE id = ?"
        self.cursor.execute(update_string, (first_name, last_name, id_))
        self.db.commit()

    def read(self, id_: int):
        select_string = f"select * from actor where id = {id_}"

        data = tuple(*self.cursor.execute(select_string))
        if data == ():
            return None
        else:
            return Actor(*data)

    def delete(self, id_):
        delete_string = f"Delete from actor where id={id_}"
        self.cursor.execute(delete_string)
        self.db.commit()

    def all(self):
        raw_data = self.cursor.execute('SELECT * From actor')
        return [Actor(*i) for i in raw_data]
