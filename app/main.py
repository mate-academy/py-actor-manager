import sqlite3

from models import Actor
from managers import ActorManager


connection = sqlite3.connect("cinema.sqlite")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE actors (id        INTEGER "
    "                              PRIMARY KEY "
    "                              UNIQUE "
    "                              NOT NULL, "
    "                      first_name TEXT, "
    "                      last_name  TEXT "
    ");"
)
connection.close()


if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
