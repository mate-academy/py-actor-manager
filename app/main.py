from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    Actor.objects.create(first_name="Emma", last_name="Watson")
    print(Actor.objects.all())
    Actor.objects.update(1, "Daniel", "Radclifffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
