from dataclasses import dataclass
from typing import Optional


@dataclass
class Actor:
    first_name: str
    last_name: str
    id: Optional[int] = None
