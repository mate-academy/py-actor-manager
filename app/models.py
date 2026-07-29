from dataclasses import dataclass


@dataclass
class Actor:
    """Represent an actor by id, first name, and last name."""

    id: int
    first_name: str
    last_name: str
