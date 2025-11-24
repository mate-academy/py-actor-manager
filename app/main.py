from managers import ActorManager
from models import Actor

if __name__ == "__main__":
    Actor.objects = ActorManager()
