import sqlite3


def initialize_database():
    connector = sqlite3.connect("cinema.db")
    cursor = connector.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    connector.commit()
    connector.close()


initialize_database()
