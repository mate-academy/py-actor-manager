from models import Actor
from managers import ActorManager

Actor.objects = ActorManager()

Actor.objects.create(first_name="Emma", last_name="Watson")
Actor.objects.create(first_name="Daniel", last_name="Radclife")
print(Actor.objects.all())
Actor.objects.update(12, "Daniel", "Radcliffe")
print(Actor.objects.all())
Actor.objects.delete(1)
print(Actor.objects.all())
