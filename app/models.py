from dataclasses import dataclass


@dataclass
class Actor:
    """Data class for representing an actor."""
    id: int
    first_name: str
    last_name: str
