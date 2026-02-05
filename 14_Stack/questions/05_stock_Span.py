# concepth of previous greater element
def main():
    arr = [100, 80, 60, 81, 70, 60, 75, 85]
    n = len(arr)
    pgi = [0] * n
    st = []

    pgi[0] = 1
    st.append(0)

    for i in range(1, n):
        while len(st) > 0 and arr[st[-1]] <= arr[i]:
            st.pop()
        if len(st) == 0:
            pgi[i] = -1
        else:
            pgi[i] = st[-1]
        pgi[i] = i - pgi[i]
        st.append(i)

    for i in range(n):
        print(pgi[i], end=" ")


if __name__ == "__main__":
    main()
