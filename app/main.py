from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.update(7, "Yura", "Zdanevych")
    print(Actor.objects.all())
