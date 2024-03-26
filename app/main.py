from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(99, "Daniel", "2Rdsffwe")
    print(Actor.objects.all())
    Actor.objects.delete(100)
    print(Actor.objects.all())
