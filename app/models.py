from dataclasses import dataclass


# add dataclass here
@dataclass
class Actor:
    first_name: str
    last_name: str

    # def __init__(self, first_name, last_name) -> None:
    #     self.first_name = first_name
    #     self.last_name = last_name
