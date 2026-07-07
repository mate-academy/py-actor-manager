from app.managers import ActorManager
from app.models import Actor

if __name__ == "__main__":
    Actor.objects = ActorManager(db_name="cinema.sqlite", table_name="actors")

    Actor.objects.create(first_name="Tom", last_name="Holland")
    Actor.objects.create(first_name="Tom", last_name="Hardy")
    print(Actor.objects.all())
    Actor.objects.update(2, "Willem", "Dafoe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
