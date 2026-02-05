graph = []
v = 0  # no. of vertices

def add_edge(src, dest, wt, bi_dir=True):
    graph[src][dest] = wt
    if bi_dir:
        graph[dest][src] = wt

def display():
    for i in range(len(graph)):
        print(f"{i} -> ", end="")
        for key, value in graph[i].items():
            print(f"({key} {value}) ", end="")
        print()

def main():
    global v, graph
    v = int(input())
    graph = [{} for _ in range(v)]
    e = int(input())
    for _ in range(e):
        s, d, wt = map(int, input().split())
        add_edge(s, d, wt)
    display()

if __name__ == "__main__":
    main()
