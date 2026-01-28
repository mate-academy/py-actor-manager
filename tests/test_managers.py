import pytest
import sqlite3

from app.managers import ActorManager
from app.models import Actor


DB_NAME = "cinema.db"
TABLE_NAME = "actors"


@pytest.fixture()
def test_db(tmp_path):
    """
    Create a temporary SQLite database file
    """
    db_file = tmp_path / DB_NAME
    conn = sqlite3.connect(str(db_file))
    conn.execute(
        f"""
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

    return str(db_file)


@pytest.fixture()
def manager(test_db):
    return ActorManager(db_name=test_db, table_name=TABLE_NAME)


def test_create(manager):
    manager.create(first_name="Brad", last_name="Pitt")
    actors = manager.all()
    assert len(actors) == 1
    assert isinstance(actors[0], Actor)
    assert actors[0].first_name == "Brad"
    assert actors[0].last_name == "Pitt"
    assert actors[0].id == 1


def test_all_empty(manager):
    actors = manager.all()
    assert len(actors) == 0
    assert isinstance(actors, list)


def test_all_multiple_actors(manager):
    test_actors = [
        ("Brad", "Pitt"),
        ("Leonardo", "DiCaprio"),
        ("Margot", "Robbie"),
    ]

    for first_name, last_name in test_actors:
        manager.create(
            first_name=first_name,
            last_name=last_name
        )

    actors = manager.all()
    assert len(actors) == 3

    for i, (first_name, last_name) in enumerate(test_actors, start=1):
        actor = next(actor for actor in actors if actor.id == i)
        assert actor.first_name == first_name
        assert actor.last_name == last_name


def test_update(manager):
    manager.create(first_name="Brad", last_name="Pitt")
    manager.update(pk=1, new_first_name="Bradley", new_last_name="Pitt")

    actors = manager.all()
    assert len(actors) == 1
    assert actors[0].first_name == "Bradley"
    assert actors[0].last_name == "Pitt"


def test_delete(manager):
    manager.create(first_name="Brad", last_name="Pitt")
    manager.create(first_name="Leonardo", last_name="DiCaprio")

    manager.delete(pk=1)
    actors = manager.all()

    assert len(actors) == 1
    assert actors[0].first_name == "Leonardo"
    assert actors[0].last_name == "DiCaprio"
