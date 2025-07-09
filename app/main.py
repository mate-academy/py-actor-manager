from managers import ActorManager


manager = ActorManager("meubanco.db", "actors")

# Criar atores
manager.create("Tom", "Cruise")
manager.create("Emma", "Watson")

# Listar todos os atores
for actor in manager.all():
    print(actor)

# Atualizar um ator (por ID)
manager.update(1, "Thomas", "Cruise")

# Deletar um ator
manager.delete(2)
