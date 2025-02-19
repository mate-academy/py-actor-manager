import sqlite3


# Define the database file name
db_name = "cinema.sqlite"

# Create a connection (this will create the file if it doesn't exist)
conn = sqlite3.connect(db_name)
conn.close()

print(f"Database '{db_name}' created successfully.")
