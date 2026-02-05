import heapq

def main():
    arr = [10, 2, 0, -4, 5, 18, 24, 1, -7, 56]
    k = 3
    n = len(arr)
    # Python's heapq is min heap, we need max heap
    # Negate values for max heap behavior
    pq = []
    for i in range(n):
        heapq.heappush(pq, -arr[i])
        if len(pq) > k:
            heapq.heappop(pq)
    print(-pq[0])

if __name__ == "__main__":
    main()
