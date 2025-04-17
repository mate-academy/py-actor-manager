# Actor manager

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

In this task, you should create a manager for the dataclass `Actor`.

#### 1. Create dataclass inside `models.py` module
`Actor` should have the following attributes:
- `id` - unique identifier for each actor
- `first_name` - actor's first name
- `last_name` - actor's last name

#### 2. Create database
Create a database `cinema` where will be stored entries with data about different actors and actresses.
Create a table `actors` with corresponding columns.
Now, you are ready to create a manager.

#### 3. Create manager inside `managers.py` module
Create `ActorManager` class that should provide **CRUD** operations. 
It should create a connection to the database inside the constructor.
The manager should have the following methods:
- `create` - a method that creates a new entry in the `actors` table
with given properties.
- `all` - a method that returns a list of `Actor` instances from DB
- `update` - a method that updates properties for entry with given `id`
- `delete` - a method that deletes entry with given `id` from DB

#### 4. Test
Test different methods in the `main.py` module.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
