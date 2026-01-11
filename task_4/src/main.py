import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2**layer
            pos[node.left.id] = (left, y - 1)
            left = add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2**layer
            pos[node.right.id] = (right, y - 1)
            right = add_edges(graph, node.right, pos, x=right, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def create_tree_heap_from_array(root: Node, nums: list, parentIndex: int) -> None:

    if len(nums) - 1 > parentIndex * 2 + 1:
        root.left = Node(nums[parentIndex * 2 + 1])
        create_tree_heap_from_array(root.left, nums, parentIndex * 2 + 1)

    if len(nums) - 1 > parentIndex * 2 + 2:
        root.right = Node(nums[parentIndex * 2 + 2])
        create_tree_heap_from_array(root.right, nums, parentIndex * 2 + 2)


def main():
    nums = [4, 10, 3, 5, 99, 10, 56, 78, 45, 96, 27, 45, 1]
    heapq.heapify(nums)

    root = Node(nums[0])

    create_tree_heap_from_array(root, nums, 0)

    print(nums)

    # # Відображення дерева
    draw_tree(root)


if __name__ == "__main__":
    main()
