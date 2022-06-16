from models import Actor
from managers import ActorManager

Actor.objects.create(name="Emma", surname="Watson")
Actor.objects.create(name="Daniel", surname="Radclife")
print(Actor.objects.all())
Actor.objects.update(40, "Daniel", "Radcliffe")
print(Actor.objects.all())
Actor.objects.delete(1)
print(Actor.objects.all())

if __name__ == "__main__":
    Actor.objects = ActorManager()
