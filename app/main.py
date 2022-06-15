from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    # Actor.objects.create(first_name="Emma", last_name="Watson")
    # Actor.objects.create(first_name="Daniel", last_name="Radclife")
    # print(Actor.objects.all())
    # Actor.objects.update(2, "Daniel", "Radcliffe")
    # print(Actor.objects.all())
    # Actor.objects.delete(5)
    # Actor.objects.delete(6)
    # print(Actor.objects.all())
