def add_edge(graph: list, src: int, dest: int, wt: int, bi_dir: bool = True) -> None:
    graph[src][dest] = wt  # Just store the weight
    if bi_dir:
        graph[dest][src] = wt


def display(graph: list) -> None:
    # Print header
    print("\n   ", end="")
    for i in range(len(graph)):
        print(f"{i:4}", end="")
    print("\n   " + "----" * len(graph))
    
    # Print matrix
    for i, row in enumerate(graph):
        print(f"{i} | ", end="")
        for cell in row:
            print(f"{cell:4}", end="")
        print()


def main():
    v = int(input("Enter no. of vertices: "))
    graph = [[0 for _ in range(v)] for _ in range(v)]  # Initialize with 0
    edges = int(input("Enter no. of edges: "))
    print("\nEnter src, dest then wt")
    for _ in range(edges):
        s, d, wt = map(int, input().split())
        add_edge(graph, s, d, wt)
    display(graph)


if __name__ == "__main__":
    main()