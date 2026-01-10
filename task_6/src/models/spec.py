class Spec:
    def __init__(self, cost: int, calories: int):
        self.cost = cost
        self.calories = calories

    def __str__(self):
        return f"Spec(cost={self.cost}, calories={self.calories})"

    def __repr__(self):
        return self.__str__()
