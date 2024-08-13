class Validate:
    def __init__(self, value: int) -> None:
        self.value = value

        self.validate = lambda x: False

    def is_valid(self) -> bool:
        return self.validate(self.value)
