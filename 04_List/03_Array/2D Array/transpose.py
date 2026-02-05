def main():
    m = int(input("Enter row/columns: "))
    # changing the same matrix to its transpose is only possible for sq. matrix
    arr = []
    print("Enter elements")
    for i in range(m):
        row = list(map(int, input().split()))
        arr.append(row)
    
    for i in range(m):
        for j in range(i + 1, m):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    print()
    for i in range(m):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
