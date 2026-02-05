def main():
    arr = [7, 1, 2, 5, 8, 4, 9, 3, 6]
    k = 3
    n = len(arr)

    maxSum = float("-inf")   # equivalent to INT_MIN
    maxIdx = -1

    for i in range(0, n - k + 1):
        s = 0
        for j in range(i, i + k):
            s += arr[j]

        if s > maxSum:
            maxSum = s
            maxIdx = i

    print(maxSum)
    print(maxIdx)


if __name__ == "__main__":
    main()
