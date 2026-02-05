# Implementation of DSU with path compresssion

def find(parent, x):
    # This method returns which group x belongs to
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a == b:  # Already in same set
        return
    
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:  # rank[a] == rank[b]
        parent[b] = a
        rank[a] += 1  # Only increment when ranks are equal

def main():
    n, m = map(int, input().split())
    # n -> number of elements, m -> number of queries
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    
    for _ in range(m):
        query = input().split()
        if query[0] == "union":
            x, y = int(query[1]), int(query[2])
            union(parent, rank, x, y)
        else:
            x = int(query[1])
            print(find(parent, x))

if __name__ == "__main__":
    main()
