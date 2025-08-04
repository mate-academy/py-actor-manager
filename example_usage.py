"""
Example usage of the ActorManager class.

This script demonstrates how to use the ActorManager to perform
CRUD operations on an SQLite database of actors.
"""

from app.managers import ActorManager

# Create a manager instance with database and table names
manager = ActorManager('actors.db', 'actors')

# Create some actors
print("Creating actors...")
actor1 = manager.create('Tom', 'Hanks')
actor2 = manager.create('Meryl', 'Streep')
actor3 = manager.create('Leonardo', 'DiCaprio')

print(f"Created: {actor1}")
print(f"Created: {actor2}")
print(f"Created: {actor3}")

# Display all actors
print("\nAll actors:")
for actor in manager.all():
    print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")

# Update an actor
print("\nUpdating actor with ID 1...")
manager.update(1, 'Thomas', 'Hanks')

# Display all actors after update
print("\nAll actors after update:")
for actor in manager.all():
    print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")

# Delete an actor
print("\nDeleting actor with ID 2...")
manager.delete(2)

# Display final list of actors
print("\nFinal list of actors:")
for actor in manager.all():
    print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")

print("\nExample completed successfully!")
