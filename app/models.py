class Actor:
    objects: any

    def __init__(
            self,
            identifier: int,
            first_name: str,
            last_name: str
    ) -> None:
        self.id = identifier
        self.first_name = first_name
        self.last_name = last_name
