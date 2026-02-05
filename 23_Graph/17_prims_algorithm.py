# Converted from prims.cpp

import heapq
from typing import List, Tuple


def add_edge(graph: List[List[Tuple[int, int]]], u: int, v: int, wt: int, bidir: bool = True) -> None:
    graph[u].append((v, wt))
    if bidir:
        graph[v].append((u, wt))


def prims(src: int, n: int, graph: List[List[Tuple[int, int]]]) -> int:
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, (0, src))
    total = 0
    while min_heap and len(visited) < n:
        wt, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total += wt
        for nei, w in graph[node]:
            if nei not in visited:
                heapq.heappush(min_heap, (w, nei))
    return total


def main():
    n = 4
    graph = [[] for _ in range(n + 1)]  # 1-based
    edges = [(1, 2, 10), (1, 3, 6), (1, 4, 5), (2, 4, 15), (3, 4, 4)]
    for u, v, wt in edges:
        add_edge(graph, u, v, wt)
    src = 1
    print(prims(src, n, graph))


if __name__ == "__main__":
    main()
