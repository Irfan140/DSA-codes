
def add_edge(graph: list, src: int, dest: int, bi_dir: bool = True) -> None:
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)


def dfs(node: int, graph: list, visited: set) -> None:
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited)


def connected_components(graph: list) -> int:
    v = len(graph)
    visited = set()
    result = 0
    for i in range(v):
        if i not in visited:
            result += 1
            dfs(i, graph, visited)
    return result


def main():
    v = 6
    graph = [[] for _ in range(v)]
    edges = [(0, 1), (2, 3), (3, 4), (4, 2)]
    for s, d in edges:
        add_edge(graph, s, d)
    print(connected_components(graph))


if __name__ == "__main__":
    main()
