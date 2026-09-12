"""Deterministic graph searches with independent snapshots for teaching.

Neighbors follow adjacency-list order. DFS pushes in reverse order so the
first neighbor is visited first. Frontier discovery prevents duplicate visits.
Queue front is at the left; stack top is at the right. A step records the
state after visiting a node and adding its neighbors (unless it is the goal).
"""

from collections import deque
from dataclasses import dataclass


@dataclass
class SearchStep:
    current: str | None
    visited_order: list[str]
    frontier: list[str]
    found: bool


@dataclass
class SearchResult:
    visited_order: list[str]
    parent: dict[str, str | None]
    path: list[str]
    history: list[SearchStep]


def _search(graph, start, goal, depth_first):
    if start not in graph or goal not in graph:
        raise ValueError("Start and goal must be graph nodes")
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("Every neighbor must be a graph node")
    frontier = deque([start])
    parent = {start: None}
    visited = []
    history = [SearchStep(None, [], [start], False)]
    path = []
    while frontier:
        current = frontier.pop() if depth_first else frontier.popleft()
        visited.append(current)
        found = current == goal
        if not found:
            neighbors = list(graph[current])
            for neighbor in reversed(neighbors) if depth_first else neighbors:
                if neighbor not in parent:
                    parent[neighbor] = current
                    frontier.append(neighbor)
        history.append(SearchStep(current, visited.copy(), list(frontier), found))
        if found:
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            break
    return SearchResult(visited, parent, path, history)


def bfs(graph, start, goal):
    """FIFO search; shortest path by edge count in an unweighted graph."""
    return _search(graph, start, goal, depth_first=False)


def dfs(graph, start, goal):
    """LIFO search; reverse pushes, mark on discovery, no shortest guarantee."""
    return _search(graph, start, goal, depth_first=True)
