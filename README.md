# Actor manager

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

In this task, you should create a manager for the dataclass `Actor`.

#### 1. Create dataclass inside `models.py` module
`Actor` should have the following attributes:
- `id` - unique identifier for each actor
- `first_name` - actor's first name
- `last_name` - actor's last name

#### 2. Create manager inside `managers.py` module
Create `ActorManager` class that should provide **CRUD** operations. 
It must take 2 parameters `db_name` and `table_name` in the `__init__` method.
It should create a connection to the database inside the `__init__` method.

The manager should have the following methods:
- `create` - a method that creates a new entry in the table.
It must take 2 parameters `first_name` and `last_name` and create a new entry in the table with given properties.

- `all` - a method that returns a list of `Actor` instances from DB. 
It must return an empty list if there are no entries in the table.

- `update` - a method that updates properties for entry with given `pk`. 
It must take 3 parameters `pk`, `new_first_name` and `new_last_name`

- `delete` - a method that deletes entry with given `pk` from DB. 
It must take 1 parameter `pk`

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
