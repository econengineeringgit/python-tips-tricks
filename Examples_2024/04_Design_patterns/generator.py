import random
from typing import Literal


class Generator:
    def __init__(self, count: int, minimum: float, maximum: float):
        self.count = count
        self.minimum = minimum
        self.maximum = maximum

    def generate(self) -> list[any]: ...


class RandomIntGenerator(Generator):
    def generate(self):
        return [
            random.randint(int(self.minimum), int(self.maximum))
            for _ in range(self.count)
        ]


class RandomFloatGenerator(Generator):
    def generate(self):
        return [random.uniform(self.minimum, self.maximum) for _ in range(self.count)]


def generate_values(
    generator: Literal["int", "float"], count: int, minimum: float, maximum: float
):
    if generator == "int":
        return RandomIntGenerator(count, minimum, maximum).generate()
    elif generator == "float":
        return RandomFloatGenerator(count, minimum, maximum).generate()
    else:
        raise ValueError("Invalid generator type")
