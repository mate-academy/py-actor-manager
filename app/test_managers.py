import pytest
import os
from app.managers import ActorManager


# Фікстура для створення менеджера
@pytest.fixture
def manager() -> ActorManager:
    db_path = "test_cinema.db"
    manager = ActorManager(db_path)
    yield manager
    manager.close()
    if os.path.exists(db_path):
        os.remove(db_path)


# Фікстура для підготовки бази даних
@pytest.fixture
def setup_database(manager: ActorManager) -> None:
    manager.cursor.execute("DROP TABLE IF EXISTS actors")
    manager.cursor.execute("""
    CREATE TABLE actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
    """)
    manager.conn.commit()


# Тест створення актора
def test_create(manager: ActorManager, setup_database: None) -> None:
    actor_id = manager.create("Tom", "Hanks")
    actors = manager.all()
    assert len(actors) == 1
    assert actors[0].id == actor_id
    assert actors[0].first_name == "Tom"
    assert actors[0].last_name == "Hanks"


# Тест оновлення актора
def test_update(manager: ActorManager, setup_database: None) -> None:
    actor_id = manager.create("Tom", "Hanks")
    manager.update(actor_id, "Thomas", "Hanks")
    actors = manager.all()
    assert len(actors) == 1
    assert actors[0].id == actor_id
    assert actors[0].first_name == "Thomas"
    assert actors[0].last_name == "Hanks"


# Тест видалення актора
def test_delete(manager: ActorManager, setup_database: None) -> None:
    actor_id = manager.create("Tom", "Hanks")
    manager.delete(actor_id)
    actors = manager.all()
    assert len(actors) == 0
