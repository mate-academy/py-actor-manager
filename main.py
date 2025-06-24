from models import Actor
from managers import ActorManager




if __name__ == "__main__":
    Actor.objects = ActorManager()

    #print(Actor.objects.all())
    print(Actor.objects.delete(1))
    #print(Actor.objects.update(18, "angelina", "Jolie"))
