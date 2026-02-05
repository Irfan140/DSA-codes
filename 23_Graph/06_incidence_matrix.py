incidenceMatrix = []


def add_edge(src, dest, edgeIndex):
    # Mark source vertex
    incidenceMatrix[src][edgeIndex] = 1
    # Mark destination vertex
    incidenceMatrix[dest][edgeIndex] = 1


def display():
    for i in range(len(incidenceMatrix)):
        for j in range(len(incidenceMatrix[0])):
            print(incidenceMatrix[i][j], end=" ")
        print()


def main():
    v = int(input("Number of vertices: "))

    e = int(input("Number of edges: "))

    # Resize incidence matrix: v rows (vertices) x e columns (edges)
    global incidenceMatrix
    incidenceMatrix = [[0 for _ in range(e)] for _ in range(v)]

    for i in range(e):
        s, d = map(int, input("Enter edge (source destination): ").split())
        add_edge(s, d, i)  # Add edge i

    print("Incidence Matrix:")
    display()


if __name__ == "__main__":
    main()
