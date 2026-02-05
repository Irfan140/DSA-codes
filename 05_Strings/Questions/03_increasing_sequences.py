# Converted from 03_increasing_sequences.cpp

from typing import List


def print_subsets(arr: List[int], idx: int, ans: List[int], k: int) -> None:
    n = len(arr)
    if idx == n:
        if len(ans) == k:
            print(" ".join(map(str, ans)))
        return

    if len(ans) + (n - idx) < k:
        return

    # Exclude current
    print_subsets(arr, idx + 1, ans, k)
    # Include current
    ans.append(arr[idx])
    print_subsets(arr, idx + 1, ans, k)
    ans.pop()


def main():
    arr = [1, 2, 3, 4, 5]
    k = 3
    print_subsets(arr, 0, [], k)


if __name__ == "__main__":
    main()
