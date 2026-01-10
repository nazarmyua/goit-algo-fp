import unittest as unittest

from task_6.src.main import greedy_algorithm, dynamic_programming
from task_6.src.models.item import Item


class TestAlgo(unittest.TestCase):

    def test_greedy_algorithm(self):
        items = [
            Item("Item1", 50, 200),
            Item("Item3", 20, 100),
            Item("Item2", 30, 120),
        ]
        budget = 70
        selected, total_cal, total_cost = greedy_algorithm(items, budget)

        self.assertEqual(total_cost <= budget, True)
        self.assertEqual(total_cal, 300)
        self.assertEqual(len(selected), 2)

    def test_dynamic_programming(self):
        items = [
            Item("Item1", 50, 200),
            Item("Item3", 20, 100),
            Item("Item2", 30, 120),
            Item("Item4", 30, 1000),
            Item("Item5", 10, 10),
        ]
        budget = 90
        selected, total_cal, total_cost = dynamic_programming(items, budget)

        self.assertEqual(total_cost <= budget, True)
        self.assertEqual(total_cal, 1230)
        print(selected)
        self.assertEqual(len(selected), 4)
