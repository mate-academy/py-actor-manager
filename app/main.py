from models import Actor
from managers import ActorManager
#
if __name__ == "__main__":
    Actor.objects = ActorManager()
#
    # Actor.objects.create(first_name_="Emma", last_name_="Watson")
    # Actor.objects.create(first_name_="Daniel", last_name_="Radclife")
    # print(Actor.objects.all())
    # Actor.objects.update(4, "Daniel", "Radcliffe")
    # print(Actor.objects.all())
    # Actor.objects.delete(3)
    # print(Actor.objects.all())
