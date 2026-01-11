from collections import deque

from node import Node
from generate_color import generate_color


def bfs(node: Node):
    step = 1
    queue = deque([node])
    while queue:
        node = queue.popleft()
        node.color = generate_color(step)
        step += 1

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
