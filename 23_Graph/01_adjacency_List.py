graph = []
v = 0  # no. of vertices


def add_edge(src, dest, bi_dir = True):
    graph[src].append(dest)
    if bi_dir:
        graph[dest].append(src)

def display():
    for i in range(len(graph)):
        print(f"{i} -> ", end="")
        for el in graph[i]:
            print(f"{el} ", end="")
        print()

def main():
    global graph, v
    print("Enter no. of Vertices: ", end="")
    v = int(input())
    graph = [[] for _ in range(v)]
    print("Enter no. of Edges: ", end="")
    e = int(input())
    for _ in range(e):
        s, d = map(int, input().split())
        add_edge(s, d)
        
    display()

if __name__ == "__main__":
    main()

# for directed graph give an extra parameter False to add_edge()
