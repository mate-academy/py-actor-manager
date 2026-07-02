from dataclasses import dataclass


@dataclass
class Actor:
    id: int             # - unique identifier for each actor
    first_name: str     # - actor's first name
    last_name: str      # - actor's last name
