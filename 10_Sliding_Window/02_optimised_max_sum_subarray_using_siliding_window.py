def main():
    arr = [7, 1, 2, 5, 8, 4, 9, 3, 6]
    k = 3
    n = len(arr)

    maxSum = float("-inf")   # INT_MIN equivalent
    maxIdx = 0
    prevSum = 0

    # find initial window sum
    for i in range(k):
        prevSum += arr[i]

    maxSum = prevSum

    i = 1   # window start
    j = k   # window end

    while j < n:
        currSum = prevSum + arr[j] - arr[i - 1]

        if currSum > maxSum:
            maxSum = currSum
            maxIdx = i

        prevSum = currSum
        i += 1
        j += 1

    print(maxSum)
    print(maxIdx)


if __name__ == "__main__":
    main()
