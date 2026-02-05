# Converted from 01_first_negative_element_in_window_of_size_k.cpp

from collections import deque


def first_negative_in_window(arr: list, k: int) -> list:
    n = len(arr)
    q = deque()  # stores indices of negative numbers
    res = []
    for i in range(n):
        if arr[i] < 0:
            q.append(i)
        if i >= k - 1:
            # remove indices out of current window
            while q and q[0] < i - k + 1:
                q.popleft()
            if q:
                res.append(arr[q[0]])
            else:
                res.append(0)
    return res


def main():
    arr = [0, -1, -2, 3, 4, -5, 6, 4, 7, -8]
    k = 3
    print(first_negative_in_window(arr, k))


if __name__ == "__main__":
    main()
