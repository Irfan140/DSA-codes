# Given a graph check whether there is a path between any two given vertices 

from collections import defaultdict

graph = []
v = 0  # no. of vertices
visited = set()

def add_edge(src, dest, bi_dir=True):
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)

def dfs(curr, end):
    if curr == end:
        return True
    visited.add(curr)  # marked visited
    for neighbour in graph[curr]:
        if neighbour not in visited:
            result = dfs(neighbour, end)
            if result:
                return True
    return False

def any_path(src, dest):
    return dfs(src, dest)

def main():
    global graph, v, visited
    v = int(input())
    graph = [[] for _ in range(v)]
    e = int(input())
    visited.clear()
    for _ in range(e):
        s, d = map(int, input().split())
        add_edge(s, d)
    x, y = map(int, input().split())
    print(any_path(x, y))

if __name__ == "__main__":
    main()

# for weighted give False to add_edge()
# solved using DFS technique
