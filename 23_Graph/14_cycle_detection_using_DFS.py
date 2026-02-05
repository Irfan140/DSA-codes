from typing import List


def add_edge(graph: List[List[int]], src: int, dest: int, bi_dir: bool = True) -> None:
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)


def dfs_cycle(src: int, parent: int, graph: List[List[int]], visited: set) -> bool:
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour in visited and neighbour != parent:
            return True
        if neighbour not in visited:
            if dfs_cycle(neighbour, src, graph, visited):
                return True
    return False


def has_cycle(graph: List[List[int]]) -> bool:
    visited = set()
    for i in range(len(graph)):
        if i not in visited:
            if dfs_cycle(i, -1, graph, visited):
                return True
    return False


def main():
    v = 5
    graph = [[] for _ in range(v)]
    edges = [(0, 1), (1, 2), (2, 0), (3, 4)]
    for s, d in edges:
        add_edge(graph, s, d)
    print(has_cycle(graph))


if __name__ == "__main__":
    main()
