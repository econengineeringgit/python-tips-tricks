import json
import os
import random
from importlib.machinery import SourceFileLoader
from typing import List


class TestValues:
    def __init__(self, values: List[float]) -> None:
        self.values = values

    def test(self) -> bool:
        return all(value < 25 for value in self.values)


def start():
    values = [random.uniform(0, 50) for _ in range(100)]
    testers = [TestValues]

    with open("plugin.json", "r", encoding="utf-8") as file:
        plugins = json.load(file)

    for plugin in plugins["plugins"]:
        module = SourceFileLoader(
            os.path.basename(plugin["path"]).split(".")[0], plugin["path"]
        ).load_module()
        testers.append(module.ExtraTester)

    for tester in testers:
        test = tester(values)
        print(f"{tester}: {test.test()}")


if __name__ == "__main__":
    start()
