import random
from collections import Counter
from typing import Dict, Tuple


def throw_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo(num_rolls: int) -> Tuple[Dict[int, int], Dict[int, float]]:
    sums = [throw_dice() for _ in range(num_rolls)]
    counts = Counter(sums)

    probabilities = {}
    for i in range(2, 13):
        if counts[i] is None:
            probabilities[i] = 0
        else:
            probabilities[i] = counts[i] / num_rolls

    return dict(counts.items()), dict(probabilities.items())


def theoretical_results() -> Dict[int, float]:

    ways = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }

    return ways


def get_rolls():
    try:
        num_rolls = int(
            input("Enter number of dice rolls (default 1000000): ") or "1000000"
        )
    except ValueError:
        print("Invalid input. Using default 1000000 rolls.")
        num_rolls = 1000000

    if num_rolls <= 0:
        print("Number of rolls must be positive. Using 1000000.")
        num_rolls = 1000000
    return num_rolls


def main() -> None:
    print("Monte Carlo Dice Simulation")
    print("=" * 50)

    num_rolls = get_rolls()

    counts, simulated = monte_carlo(num_rolls)
    theoretical = theoretical_results()

    print("\n" + "=" * 80)
    print("MONTE CARLO DICE SIMULATION RESULTS")
    print("=" * 80)
    print(
        f"{'Sum':<5} {'Count':<12} {'Simulated %':<15} {'Theoretical %':<15} {'Difference':<10}"
    )
    print("-" * 80)

    for s in range(2, 13):
        count = counts[s]
        simulated_proc = simulated[s] * 100
        theoretical_proc = theoretical[s] * 100
        diff = abs(simulated_proc - theoretical_proc)
        print(
            f"{s:<5} {count:<12} {simulated_proc:<15.2f} {theoretical_proc:<15.2f} {diff:<10.2f}"
        )

    print("=" * 80)


if __name__ == "__main__":
    main()
