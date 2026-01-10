from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def merge_sorted_lists(self, l2):
        merged_list = LinkedList()

        while self.head is not None and l2.head is not None:
            if self.head.data <= l2.head.data:
                merged_list.insert_at_end(self.head.data)
                self.head = self.head.next
            else:
                merged_list.insert_at_end(l2.head.data)
                l2.head = l2.head.next

        while self.head is not None:
            merged_list.insert_at_end(self.head.data)
            self.head = self.head.next

        while l2.head is not None:
            merged_list.insert_at_end(l2.head.data)
            l2.head = l2.head.next

        return merged_list
