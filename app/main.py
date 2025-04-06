from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
