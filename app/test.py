from managers import ActorManager
# from models import Actor

manager = ActorManager("../identifier.sqlite", "Users")

# actor = Actor(id=1, first_name="Kuba", last_name="Wojewódzki")
# a1 = Actor("Tomasz","Karolak")
# a2 = Actor(id=3, first_name="Jan", last_name="Kowalski")
# manager.create("Tomasz","Karolak")
# manager.add_actor(a2)

for actors in manager.all():
    print(actors)

manager.update(3, "Zbyszek", "Król")

print("\nPo zmianie\n")
for actors in manager.all():
    print(actors)

manager.delete(3)

print("\nPo usunięciu\n")
for actors in manager.all():
    print(actors)
