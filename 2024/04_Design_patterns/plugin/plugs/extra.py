from typing import List


class ExtraTester:
    def __init__(self, values: List[float]) -> None:
        self.values = values

    def test(self) -> bool:
        higher_than_25 = [value for value in self.values if value > 25]
        return len(higher_than_25) > 10
