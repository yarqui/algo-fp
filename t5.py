import uuid
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, List
from collections import deque


class Node:
    def __init__(self, val: int, color: str = "#1a1a80"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val: int = val
        self.color: str = color
        self.id: str = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: dict, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree_with_colors(
    tree_root: Node, title: str = "Binary Tree Traversal"
) -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2000,
        node_color=colors,
        font_color="white",
    )
    plt.suptitle(title, fontsize=16, fontweight="bold", color="#333333")
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave room for title
    plt.show()


def hex_color_gradient(start: str, end: str, steps: int) -> List[str]:
    """Generates a gradient list from start to end hex color."""

    def hex_to_rgb(hex_color: str) -> List[int]:
        hex_color = hex_color.lstrip("#")
        return [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]

    def rgb_to_hex(rgb: List[int]) -> str:
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    start_rgb = hex_to_rgb(start)
    end_rgb = hex_to_rgb(end)
    gradient = []

    for i in range(steps):
        interpolated = [
            int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * i / (steps - 1))
            for j in range(3)
        ]
        gradient.append(rgb_to_hex(interpolated))

    return gradient


def bfs(root: Node) -> None:
    queue = deque([root])
    visited = []
    while queue:
        current = queue.popleft()
        visited.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    gradient = hex_color_gradient("#1a1a80", "#aaccff", len(visited))
    for i, node in enumerate(visited):
        node.color = gradient[i]


def dfs(root: Node) -> None:
    stack = [root]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        # Right goes first so left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    gradient = hex_color_gradient("#1a1a80", "#aaccff", len(visited))
    for i, node in enumerate(visited):
        node.color = gradient[i]


# Sample binary tree
root_dfs = Node(0)
root_dfs.left = Node(4)
root_dfs.left.left = Node(5)
root_dfs.left.right = Node(10)
root_dfs.right = Node(1)
root_dfs.right.left = Node(3)

# Deep copy to have an identical tree structure for BFS
import copy

root_bfs = copy.deepcopy(root_dfs)

# DFS traversal visualization
dfs(root_dfs)
draw_tree_with_colors(root_dfs, "DFS Traversal Order")

# BFS traversal visualization
bfs(root_bfs)
draw_tree_with_colors(root_bfs, "BFS Traversal Order")
