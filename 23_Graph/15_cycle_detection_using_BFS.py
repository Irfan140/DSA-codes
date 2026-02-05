from collections import deque


def add_edge(graph: list, src: int, dest: int, bi_dir: bool = True) -> None:
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)


def bfs_cycle(src: int, graph: list, visited: set) -> bool:
    from collections import deque
    q = deque([src])
    parent = {src: -1}
    visited.add(src)
    while q:
        curr = q.popleft()
        for neighbour in graph[curr]:
            if neighbour in visited and parent[curr] != neighbour:
                return True
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = curr
                q.append(neighbour)
    return False


def has_cycle(graph: list) -> bool:
    visited = set()
    for i in range(len(graph)):
        if i not in visited:
            if bfs_cycle(i, graph, visited):
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
