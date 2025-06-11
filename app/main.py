from app.models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    Actor.objects.create(first_name="Donald", last_name="Dak")
    Actor.objects.create(first_name="Brad", last_name="Pitt")
    print(Actor.objects.all())
    Actor.objects.update(2, "Brad", "Pitt")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
