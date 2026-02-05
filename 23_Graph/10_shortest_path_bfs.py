# Solved using BFS

from collections import deque

graph = []
v = 0  # no. of vertices
visited = set()


def add_edge(src, dest, bi_dir=True):
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)


def bfs(src, dest, dist):
    qu = deque()
    visited.clear()
    dist.clear()
    dist.extend([float("inf")] * v)

    dist[src] = 0
    visited.add(src)
    qu.append(src)

    while qu:
        curr = qu.popleft()
        for neighbour in graph[curr]:
            if neighbour not in visited:
                qu.append(neighbour)
                visited.add(neighbour)
                dist[neighbour] = dist[curr] + 1


def main():
    global v, graph

    v = int(input())
    graph = [[] for _ in range(v)]

    e = int(input())
    visited.clear()

    while e > 0:
        s, d = map(int, input().split())
        add_edge(s, d)
        e -= 1

    x, y = map(int, input().split())

    dist = []
    bfs(x, y, dist)

    for d in dist:
        print(d, end=" ")


if __name__ == "__main__":
    main()
