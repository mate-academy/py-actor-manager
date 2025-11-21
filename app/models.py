from dataclasses import dataclass


@dataclass
class Actor:
    """
    Represents an actor with identifying information.

    Attributes:
        id (int): Unique identifier for the actor.
        first_name (str): Actor's first name.
        last_name (str): Actor's last name.
    """
    id: int
    first_name: str
    last_name: str
