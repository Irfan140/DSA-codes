import heapq
from collections import defaultdict

gr = []

def add_edge(u, v, wt, bidir=True):
    gr[u].append((v, wt))
    if bidir:
        gr[v].append((u, wt))

def dijkstra(src, n):
    pq = [(0, src)]  # (distance, node)
    vis = set()
    via = [0] * n
    mp = {i: float('inf') for i in range(n)}
    mp[src] = 0
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_node in vis:
            continue
        
        vis.add(curr_node)
        
        for neighbour, weight in gr[curr_node]:
            if neighbour not in vis and mp[neighbour] > mp[curr_node] + weight:
                heapq.heappush(pq, (mp[curr_node] + weight, neighbour))
                via[neighbour] = curr_node
                mp[neighbour] = mp[curr_node] + weight
    
    return mp

def main():
    global gr
    n, m = map(int, input().split())
    gr = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, wt = map(int, input().split())
        add_edge(u, v, wt)
    
    src = int(input())
    sp = dijkstra(src, n)
    dest = int(input())
    print(sp[dest])

if __name__ == "__main__":
    main()

# print via to get all the shortest distance of src and other nodes
