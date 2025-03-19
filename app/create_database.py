import sqlite3


conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
    )
""")
conn.commit()
conn.close()
