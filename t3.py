import heapq
from typing import Dict, List, Tuple


class Graph:
    def __init__(self):
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int) -> None:
        """
        Adds a directed edge from node u to node v with the given weight.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[v].append((u, weight))

    def dijkstra(self, start: str) -> Dict[str, int]:
        """
        Performs Dijkstra's algorithm using a binary heap to find shortest paths from `start`.
        Returns a dictionary of distances from start to each reachable vertex.
        """
        distances: Dict[str, int] = {node: float("inf") for node in self.adjacency_list}
        distances[start] = 0

        min_heap: List[Tuple[int, str]] = [(0, start)]

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list.get(current_node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances


# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "E", 3)

    start_node = "A"
    shortest_paths = graph.dijkstra(start_node)

    print(f"Shortest distances from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"  {node}: {distance}")
