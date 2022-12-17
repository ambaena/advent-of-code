from collections import deque
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass(frozen=True)
class Cord:
    x: int
    y: int

    def get_neighbours(self):
        return [Cord(self.x + 1, self.y), Cord(self.x - 1, self.y), Cord(self.x, self.y + 1), Cord(self.x, self.y - 1)]


def _get_graph(input: List) -> Tuple[Dict, Cord, Cord]:
    graph = {}
    for r, row in enumerate(input):
        for c, value in enumerate(row):
            if value in 'S':
                start = Cord(r, c)
                value = 'a'
            if value == 'E':
                end = Cord(r, c)
                value = 'z'
            graph[Cord(r, c)] = value
    return graph, start, end


def BFS(graph: Dict[Cord, str], node: Cord, end: Cord) -> int:
    visited, queue = set(), deque([[node, 0]])
    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps
        for neighbour in node.get_neighbours():
            if neighbour not in visited and neighbour in graph and (ord(graph[neighbour]) - ord(graph[node]) <= 1):
                visited.add(neighbour)
                queue.append([neighbour, steps + 1])


def solution_one(input: str) -> int:
    """it seems to be an BFS algorith."""
    input = [[*row] for row in input.split('\n')]
    graph, start, end = _get_graph(input)
    return BFS(graph, start, end)


def solution_two(input: str) -> int:
    """it seems to be an BFS algorith."""
    input = [[*row] for row in input.split('\n')]
    graph, start, end = _get_graph(input)
    return min(filter(lambda item: item is not None, [BFS(graph, node, end) for node in graph if graph[node] == 'a']))


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
