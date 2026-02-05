import heapq

def main():
    # original values
    arr = [1, 80, 3, -4]

    # MIN HEAP
    min_heap = []
    for x in arr:
        heapq.heappush(min_heap, x)

    print("Min heap list:", min_heap)
    print("Min element:", min_heap[0])

    # MAX HEAP (store negatives to demonstrate it)
    max_heap = []
    for x in arr:
        heapq.heappush(max_heap, -x)

    print("Max heap list (stored as negatives):", max_heap)
    print("Max element:", -max_heap[0])


if __name__ == "__main__":
    main()
