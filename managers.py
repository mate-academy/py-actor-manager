import sqlite3
class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        # You'll need to create the table here too
    
    def create(self, first_name, last_name):
        # Insert a new actor
        pass
    
    def all(self):
        # Return list of Actor instances
        pass
    
    def update(self, pk, new_first_name, new_last_name):
        # Update by id
        pass
    
    def delete(self, pk):
        # Delete by id
        pass
