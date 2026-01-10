from typing import List, Tuple

from .models.item import Item


def greedy_algorithm(items: List[Item], budget: int) -> Tuple[List[Item], int, int]:
    ranked = sorted(items, key=lambda item: item.rafio, reverse=True)

    selected: List[Item] = []
    total_cal = 0
    total_cost = 0
    remaining = budget

    for item in ranked:
        if item.spec.cost <= remaining:
            selected.append(item)
            total_cal += item.spec.calories
            total_cost += item.spec.cost
            remaining -= item.spec.cost

    return selected, total_cal, total_cost


def dynamic_programming(items: List[Item], budget: int) -> Tuple[List[Item], int, int]:
    n = len(items)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        itm = items[i - 1]
        cost = itm.spec.cost
        cal = itm.spec.calories
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if cost <= w:
                cand = dp[i - 1][w - cost] + cal
                if cand > dp[i][w]:
                    dp[i][w] = cand

    w = budget
    selected: List[Item] = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            itm = items[i - 1]
            selected.append(itm)
            w -= itm.spec.cost

    selected.reverse()
    total_cal = dp[n][budget]
    total_cost = sum(it.spec.cost for it in selected)
    return selected, total_cal, total_cost


def get_budget():
    while True:
        try:
            budget = int(input("Enter budget: "))
            return budget
        except ValueError:
            print("Invalid input")


def main() -> None:
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    items_list = list(
        map(
            lambda item: Item(item[0], item[1]["cost"], item[1]["calories"]),
            items.items(),
        )
    )

    budget = get_budget()

    print("\nGreedy algorithm (by calories/cost):")
    sel_g, cal_g, cost_g = greedy_algorithm(items_list, budget)
    print("Selected:")
    for item in sel_g:
        print(item)
    print(f"\nTotal calories: {cal_g}, Total cost: {cost_g}\n")

    print("\nDynamic programming (optimal):")
    sel_dp, cal_dp, cost_dp = dynamic_programming(items_list, budget)
    print("Selected:")
    for item in sel_dp:
        print(item)
    print(f"\nTotal calories: {cal_dp}, Total cost: {cost_dp}\n")


if __name__ == "__main__":
    main()
