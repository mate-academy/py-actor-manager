import os
import pytest
from app.managers import ActorManager
from app.models import Actor

TABLE_NAME = 'actors'


@pytest.fixture()
def test_db(tmp_path):
    return tmp_path / 'test.db'


@pytest.fixture()
def manager(test_db):
    return ActorManager(db_name=str(test_db), table_name=TABLE_NAME)


def test_create(manager: ActorManager):
    manager.create(first_name='Brad', last_name='Pitt')
    actors = manager.all()
    assert len(actors) == 1
    actor = actors[0]
    assert actor.first_name == 'Brad'
    assert actor.last_name == 'Pitt'
    assert actor.id == 1


def test_all_empty(manager: ActorManager):
    actors = manager.all()
    assert actors == []


def test_all_multiple_actors(manager: ActorManager):
    test_actors = [
        ('Brad', 'Pitt'),
        ('Leonardo', 'DiCaprio'),
        ('Margot', 'Robbie')
    ]
    for first_name, last_name in test_actors:
        manager.create(first_name=first_name, last_name=last_name)

    actors = manager.all()
    assert len(actors) == 3
    for i, (first_name, last_name) in enumerate(test_actors, start=1):
        actor = next(a for a in actors if a.id == i)
        assert actor.first_name == first_name
        assert actor.last_name == last_name


def test_update(manager: ActorManager):
    manager.create(first_name='Brad', last_name='Pitt')
    manager.update(pk=1, new_first_name='Bradley', new_last_name='Pitt')
    actor = manager.all()[0]
    assert actor.first_name == 'Bradley'
    assert actor.last_name == 'Pitt'


def test_delete(manager: ActorManager):
    manager.create(first_name='Brad', last_name='Pitt')
    manager.create(first_name='Leonardo', last_name='DiCaprio')
    manager.delete(pk=1)
    actors = manager.all()
    assert len(actors) == 1
    assert actors[0].first_name == 'Leonardo'
