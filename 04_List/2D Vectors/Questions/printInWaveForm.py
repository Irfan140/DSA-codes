def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        if i % 2 != 0:
            for j in range(2, -1, -1):
                print(arr[i][j], end=" ")
            print()
        else:
            for j in range(3):
                print(arr[i][j], end=" ")
            print()

if __name__ == "__main__":
    main()
