from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager(table_actors="actors")

    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(10, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
