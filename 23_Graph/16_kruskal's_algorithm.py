"""Converted from kruskal's.cpp — original C++ removed."""

from typing import List, Tuple


def find(parent: List[int], a: int) -> int:
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent: List[int], rank: List[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    if rank[a] >= rank[b]:
        rank[a] += 1
        parent[b] = a
    else:
        rank[b] += 1
        parent[a] = b


def kruskals(edges: List[Tuple[int, int, int]], n: int) -> int:
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [1] * (n + 1)
    edge_count = 0
    ans = 0
    i = 0
    while edge_count < n - 1 and i < len(edges):
        src, dest, wt = edges[i]
        src_par = find(parent, src)
        dest_par = find(parent, dest)
        if src_par != dest_par:
            union(parent, rank, src_par, dest_par)
            ans += wt
            edge_count += 1
        i += 1
    return ans


def main():
    n = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4),
    ]
    print(kruskals(edges, n))


if __name__ == "__main__":
    main()
