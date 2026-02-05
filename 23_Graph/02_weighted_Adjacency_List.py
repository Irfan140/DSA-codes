
def add_edge(graph: list, src: int, dest: int, wt: int, bi_dir: bool = True) -> None:
    graph[src].append((dest, wt))
    if bi_dir:
        graph[dest].append((src, wt))


# enumerate() adds a counter to an iterable and returns it as an enumerate object.
def display(graph: list) -> None:
    for i, nbrs in enumerate(graph):
        print(f"{i} -> ", end="")
        for dest, wt in nbrs:
            print(f"({dest} {wt}) , ", end="")
        print()


# dsiplay function without using enumerate
"""
def display(graph: list) -> None:
    for i in range(len(graph)):
    print(f"{i} -> ", end="")
    for dest, wt in graph[i]:
        print(f"({dest} {wt}) , ", end="")
    print()

"""

def main():
    v = int(input("Enter no. of vertices: "))
    graph = [[] for _ in range(v)]
    edges = int(input("Enter no. of edges: "))
    print("Enter src, dest then weight: ")
    for _ in range(edges):
        s, d, wt = map(int, input().split())
        add_edge(graph, s, d, wt)
    display(graph)


if __name__ == "__main__":
    main()
