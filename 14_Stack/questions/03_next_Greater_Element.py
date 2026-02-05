def main():
    arr = [3, 1, 2, 7, 4, 6, 2, 3]
    n = len(arr)
    ans = [0] * n
    st = []

    ans[n - 1] = -1
    st.append(arr[n - 1])

    for i in range(n - 2, -1, -1):
        while len(st) > 0 and arr[i] >= st[-1]:
            st.pop()
        if len(st) == 0:
            ans[i] = -1
        else:
            ans[i] = st[-1]
        st.append(arr[i])

    for i in range(n):
        print(ans[i], end=" ")


if __name__ == "__main__":
    main()
