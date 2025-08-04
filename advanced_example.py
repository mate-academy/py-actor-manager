"""
Advanced example usage of the ActorManager class.

This script demonstrates more advanced usage patterns and error handling.
"""

from app.managers import ActorManager
from app.models import Actor

def main():
    # Create a manager instance
    manager = ActorManager('advanced_actors.db', 'actors')
    
    print("🎬 Advanced ActorManager Demo")
    print("=" * 40)
    
    # Batch create actors
    actors_to_add = [
        ('Robert', 'De Niro'),
        ('Al', 'Pacino'),
        ('Marlon', 'Brando'),
        ('Jack', 'Nicholson'),
        ('Morgan', 'Freeman')
    ]
    
    print("\n📝 Adding actors to database:")
    for first_name, last_name in actors_to_add:
        new_actor = manager.create(first_name, last_name)
        print(f"   ✓ Added {new_actor.first_name} {new_actor.last_name} (ID: {new_actor.id})")
    
    # Display all actors with formatting
    print("\n🎭 Current actors in database:")
    actors = manager.all()
    for actor in actors:
        print(f"   #{actor.id:2d} | {actor.first_name} {actor.last_name}")
    
    print(f"\n📊 Total actors: {len(actors)}")
    
    # Update an actor
    print("\n✏️  Updating actor...")
    manager.update(1, 'Roberto', 'De Niro')
    print("   ✓ Updated Robert to Roberto")
    
    # Show specific actor after update
    updated_actors = manager.all()
    updated_actor = next(a for a in updated_actors if a.id == 1)
    print(f"   Updated actor: {updated_actor.first_name} {updated_actor.last_name}")
    
    # Delete multiple actors
    print("\n🗑️  Removing some actors...")
    actors_to_remove = [3, 5]  # Marlon Brando and Morgan Freeman
    for actor_id in actors_to_remove:
        manager.delete(actor_id)
        print(f"   ✓ Removed actor with ID {actor_id}")
    
    # Final state
    print("\n🎭 Final actors in database:")
    final_actors = manager.all()
    for actor in final_actors:
        print(f"   #{actor.id:2d} | {actor.first_name} {actor.last_name}")
    
    print(f"\n📊 Final count: {len(final_actors)} actors")
    print("\n🎉 Advanced demo completed!")

if __name__ == "__main__":
    main()
