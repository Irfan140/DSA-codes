# sort a nearly sorted array

import heapq


def sort_k_sorted(arr: list, k: int) -> list:
    n = len(arr)
    heap = []
    res = []
    for i in range(n):
        heapq.heappush(heap, arr[i])
        if len(heap) > k:
            res.append(heapq.heappop(heap))
    while heap:
        res.append(heapq.heappop(heap))
    return res


def main():
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print(sort_k_sorted(arr, k))


if __name__ == "__main__":
    main()
