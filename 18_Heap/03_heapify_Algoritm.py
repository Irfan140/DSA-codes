# Converted given array to a minheap

def print_arr(arr: list) -> None:
    for i in range(1, len(arr)):
        print(arr[i], end=" ")
    print()


def heapify(i: int, arr: list) -> None:
    n = len(arr)
    while True:
        left = 2 * i
        right = 2 * i + 1
        if left >= n:
            break
        if right >= n:
            if arr[i] > arr[left]:
                arr[i], arr[left] = arr[left], arr[i]
            break
        # Both children exist
        if arr[left] < arr[right]:
            if arr[i] > arr[left]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                break
        else:
            if arr[i] > arr[right]:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
            else:
                break


def main():
    arr = [-1, 10, 2, 14, 11, 1, 4]
    n = len(arr)
    for i in range(n // 2, 0, -1):
        heapify(i, arr)
    print_arr(arr)


if __name__ == "__main__":
    main()
