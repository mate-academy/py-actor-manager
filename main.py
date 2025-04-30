from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    Actor.objects.create(first_name="Bob", last_name="Blak")
    Actor.objects.create(first_name="Ron", last_name="Red")
    Actor.objects.create(first_name="Whill", last_name="White")
    print(Actor.objects.all())
    Actor.objects.update(13, "Gram", "Green")
    Actor.objects.update(3, "Peter", "Pink")
    print(Actor.objects.all())
    Actor.objects.delete(13)
    print(Actor.objects.all())
