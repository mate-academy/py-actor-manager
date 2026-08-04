import sqlite3


def init_db(db_name: str = "cinema.db") -> None:
    connection = sqlite3.connect(db_name)
    connection.execute(
        "CREATE TABLE IF NOT EXISTS actors ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "first_name VARCHAR(255), "
        "last_name VARCHAR(255))"
    )
    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
