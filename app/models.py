from dataclasses import dataclass


@dataclass(slots=True)
class Actor:
    id: int
    first_name: str
    last_name: str

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
