from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.start(first_name="ja", last_name="ja")
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radclife")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
