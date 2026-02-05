# Given a graph. Calculate all paths between two given nodes

graph = []
v = 0  # no. of vertices
visited = set()
result = []

def add_edge(src, dest, bi_dir=True):
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)

def dfs(curr, end, path):
    if curr == end:
        path.append(curr)
        result.append(path[:])
        path.pop()
        return
    visited.add(curr)  # marked visited
    path.append(curr)
    for neighbour in graph[curr]:
        if neighbour not in visited:
            dfs(neighbour, end, path)
    path.pop()
    visited.discard(curr)

def all_path(src, dest):
    v = []
    dfs(src, dest, v)

def main():
    global graph, v, visited, result
    v = int(input())
    graph = [[] for _ in range(v)]
    e = int(input())
    visited.clear()
    for _ in range(e):
        s, d = map(int, input().split())
        add_edge(s, d)
    x, y = map(int, input().split())
    all_path(x, y)
    for path in result:
        for el in path:
            print(el, end=" ")
        print()

if __name__ == "__main__":
    main()

# solved using DFS technique
