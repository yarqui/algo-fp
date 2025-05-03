import heapq
import matplotlib.pyplot as plt
import networkx as nx
import uuid
from typing import Optional, List


class Node:
    def __init__(self, key: int, color: str = "skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def array_to_binary_tree(heap_array: List[int], index: int = 0) -> Optional[Node]:
    """Recursively converts a heap array into a binary tree of Node objects."""
    if index >= len(heap_array):
        return None

    node = Node(heap_array[index])
    node.left = array_to_binary_tree(heap_array, 2 * index + 1)
    node.right = array_to_binary_tree(heap_array, 2 * index + 2)
    return node


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: dict, x=0, y=0, layer=1):
    """Recursively adds nodes and edges to the graph with positions."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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


def draw_tree(tree_root: Node) -> None:
    """Visualizes the binary tree using networkx and matplotlib."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node: data["label"] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2000,
        node_color=colors,
        font_size=12,
    )
    plt.title("Visualized Binary Heap as Tree")
    plt.show()


if __name__ == "__main__":
    heap_data = [10, 3, 5, 1, 4, 8]

    heapq.heapify(heap_data)
    print("Heapified list:", heap_data)

    tree_root = array_to_binary_tree(heap_data)

    draw_tree(tree_root)
