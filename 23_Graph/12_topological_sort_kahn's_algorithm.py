from collections import deque

graph = []
v = 0  # no. of edges (actually vertices)


def add_edge(a, b, bi_dir=True):
    graph[a].append(b)
    if bi_dir:
        graph[b].append(a)


def topBFS():
    indegree = [0] * v
    for i in range(v):
        for neighbour in graph[i]:
            # i -> neighbour
            indegree[neighbour] += 1

    qu = deque()
    visited = set()

    for i in range(v):
        if indegree[i] == 0:
            qu.append(i)
            visited.add(i)

    while qu:
        node = qu.popleft()
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    qu.append(neighbour)
                    visited.add(neighbour)


def main():
    global v, graph
    v = int(input())
    e = int(input())

    graph = [[] for _ in range(v)]

    while e > 0:
        x, y = map(int, input().split())
        add_edge(x, y, False)
        e -= 1

    topBFS()


if __name__ == "__main__":
    main()
