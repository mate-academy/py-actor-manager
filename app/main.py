from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name_of="Emma", last_name_of="Watson")
    Actor.objects.create(first_name_of="Daniel", last_name_of="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
