def change2D(arr):
    arr[0][0] = 100

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(arr[0][0])
    change2D(arr)
    print(arr[0][0])

if __name__ == "__main__":
    main()
