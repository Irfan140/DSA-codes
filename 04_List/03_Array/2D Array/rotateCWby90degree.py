def main():
    m = int(input("Enter row/columns: "))
    arr = []
    print("Enter elements:")
    for i in range(m):
        row = list(map(int, input().split()))
        arr.append(row)
    
    # Transpose the matrix
    for i in range(m):
        for j in range(i + 1, m):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    # Reverse each row (column in original)
    for k in range(m):
        i = 0
        j = m - 1
        while i <= j:
            arr[k][i], arr[k][j] = arr[k][j], arr[k][i]
            i += 1
            j -= 1
    
    print()
    for i in range(m):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
