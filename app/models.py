from dataclasses import dataclass


# add dataclass here
@dataclass
class Actor:
    id: int  # noqa: VNE003
    first_name: str
    last_name: str
