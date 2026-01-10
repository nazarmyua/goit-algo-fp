import unittest as unittest

from task_1.src.models.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedList()

    def test_bubble_sort(self):
        self.queue.insert_at_end(64)
        self.queue.insert_at_end(34)
        self.queue.insert_at_end(25)
        self.queue.insert_at_end(12)
        self.queue.insert_at_end(22)
        self.queue.insert_at_end(11)
        self.queue.insert_at_end(90)

        self.queue.bubble_sort()

        sorted_elements = []
        current = self.queue.head
        while current:
            sorted_elements.append(current.data)
            current = current.next

        self.assertEqual(sorted_elements, [11, 12, 22, 25, 34, 64, 90])

    def test_merge_sorted_lists(self):
        llist1 = LinkedList()
        llist1.insert_at_end(1)
        llist1.insert_at_end(3)
        llist1.insert_at_end(5)

        llist2 = LinkedList()
        llist2.insert_at_end(2)
        llist2.insert_at_end(4)
        llist2.insert_at_end(6)

        merged_list = llist1.merge_sorted_lists(llist2)

        merged_elements = []
        current = merged_list.head
        while current:
            merged_elements.append(current.data)
            current = current.next

        self.assertEqual(merged_elements, [1, 2, 3, 4, 5, 6])

    def test_reverse(self):
        self.queue.insert_at_end(1)
        self.queue.insert_at_end(2)
        self.queue.insert_at_end(3)
        self.queue.insert_at_end(4)
        self.queue.insert_at_end(5)

        self.queue.reverse()

        reversed_elements = []
        current = self.queue.head
        while current:
            reversed_elements.append(current.data)
            current = current.next

        self.assertEqual(reversed_elements, [5, 4, 3, 2, 1])
