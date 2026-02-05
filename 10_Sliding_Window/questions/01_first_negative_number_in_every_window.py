def main():
    arr = [2, -3, 4, 4, -7, -1, 4, -2, 6]
    n = len(arr)
    k = 3   # you can change to 4 also

    ans = []

    # Finding first negative in first window
    p = -1
    for i in range(k):
        if arr[i] < 0:
            p = i
            break

    if p != -1:
        ans.append(arr[p])
    else:
        ans.append(0)   # or -1

    i = 1
    j = k

    while j <= n - 1:
        # if p went out of window
        if p < i:
            p = -1
            for idx in range(i, j + 1):
                if arr[idx] < 0:
                    p = idx
                    break

        if p != -1:
            ans.append(arr[p])
        else:
            ans.append(0)

        i += 1
        j += 1

    for x in ans:
        print(x, end=" ")


if __name__ == "__main__":
    main()
