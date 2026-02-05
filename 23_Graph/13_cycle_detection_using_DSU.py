def find(parent, x):
    # This method returns which group x belongs to
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def Union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return True  # means cycle exits

    if rank[a] >= rank[b]:
        rank[a] += 1
        parent[b] = a
    else:
        rank[b] += 1
        parent[a] = b

    return False


def main():
    n = int(input())
    m = int(input())
    # n -> number of elements, m -> number of queries

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    for i in range(n + 1):
        parent[i] = i

    while m > 0:
        x, y = map(int, input().split())
        b = Union(parent, rank, x, y)
        if b:
            print("Cycle detected")
        m -= 1


if __name__ == "__main__":
    main()
