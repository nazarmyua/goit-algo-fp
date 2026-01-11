from node import Node
from generate_color import generate_color


def dfs(node: Node):
    step = 1
    stack = [node]
    while stack:
        # Вилучаємо вершину зі стеку
        node = stack.pop()

        node.color = generate_color(step)
        step += 1

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)
