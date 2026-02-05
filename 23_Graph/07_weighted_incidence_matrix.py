"""Converted from weighted_incidence_matrix.cpp — original C++ removed."""

def add_edge(incidence_matrix: list, src: int, dest: int, weight: int, edge_index: int) -> None:
    incidence_matrix[src][edge_index] = (weight, 1)
    incidence_matrix[dest][edge_index] = (weight, -1)


def display(incidence_matrix: list) -> None:
    for row in incidence_matrix:
        print(" ".join(f"({w},{d})" for w, d in row))


def main():
    v = 4
    e = 3
    incidence_matrix = [[(0, 0) for _ in range(e)] for _ in range(v)]
    edges = [(0, 1, 5), (1, 2, 3), (2, 3, 7)]
    for i, (s, d, w) in enumerate(edges):
        add_edge(incidence_matrix, s, d, w, i)
    print("Weighted Incidence Matrix:")
    display(incidence_matrix)


if __name__ == "__main__":
    main()
