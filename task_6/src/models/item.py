from .spec import Spec


class Item:
    def __init__(self, name: str, cost: int, calories: int):
        self.name = name
        self.spec = Spec(cost, calories)
        self.rafio = calories / cost

    def __str__(self):
        return f"Item(name={self.name}, {self.spec}, rafio={self.rafio:.2f})"

    def __repr__(self):
        return self.__str__()
