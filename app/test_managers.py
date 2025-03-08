import pytest
import sqlite3
from app.managers import ActorManager

@pytest.fixture
def manager():
    """Создаёт новую БД и таблицу перед тестами"""
    # Создаем временную базу данных в памяти
    conn = sqlite3.connect(":memory:")  # Для тестов используется база данных в памяти
    cursor = conn.cursor()

    # Создаем таблицу, если её нет
    cursor.execute('''CREATE TABLE actors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL
                    )''')
    conn.commit()

    # Возвращаем объект ActorManager с подключением к БД
    return ActorManager(conn)

# Пример теста
def test_create_actor(manager):
    actor_id = manager.create("John", "Doe")
    actors = manager.all()
    assert len(actors) == 1
    assert actors[0]["first_name"] == "John"
    assert actors[0]["last_name"] == "Doe"
