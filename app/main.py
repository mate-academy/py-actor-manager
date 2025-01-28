from models import Actor
from manager import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create("Emma", "Watson")
    Actor.objects.create("Daniel", "Radclife")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
