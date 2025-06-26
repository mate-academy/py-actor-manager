from dataclasses import dataclass
from django.db import models


# add dataclass here
@dataclass
class Actor:
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # def __init__(self, first_name, last_name) -> None:
    #     self.first_name = first_name
    #     self.last_name = last_name
