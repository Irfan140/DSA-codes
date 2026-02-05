def add_edge(graph: dict, src, dest, wt, bi_dir: bool = True) -> None:
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []
    
    graph[src].append((dest, wt))
    if bi_dir:
        graph[dest].append((src, wt))


def display(graph: dict) -> None:
    for vertex, nbrs in graph.items():
        print(f"{vertex} -> ", end="")
        for dest, wt in nbrs:
            print(f"({dest} {wt}) , ", end="")
        print()


def main():
    graph = {}  # Use dictionary instead of list
    edges = int(input("Enter no. of edges: "))
    print("Enter src, dest then weight: ")
    for _ in range(edges):
        # Can now use ANY vertex names (strings, ints, etc.)
        s, d, wt = input().split()
        add_edge(graph, s, d, wt)
    display(graph)
    print(graph)

if __name__ == "__main__":
    main()