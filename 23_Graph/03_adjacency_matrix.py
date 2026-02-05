graph = []

def add_edge(src, dest, bi_dir = True):
    graph[src][dest] = 1
    if bi_dir:
        graph[dest][src] = 1

def display():
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end=" ")
        print()

def main():
    global graph
    v = int(input("Number of vertices: "))
    graph = [[0] * v for _ in range(v)]
    
    e = int(input("Number of edges: "))
    for _ in range(e):
        s, d = map(int, input().split())
        add_edge(s, d)
    display()

if __name__ == "__main__":
    main()

# for unweighted undirected graph
