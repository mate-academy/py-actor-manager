from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str


if __name__ == '__main__':
    example = Actor(id=None, first_name="fn", last_name="ln")
    print(example)
