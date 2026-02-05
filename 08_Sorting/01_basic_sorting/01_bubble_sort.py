def main():
    arr = [5, 4, 6, 3, 2, 1]
    n = 6
    for i in range(n - 1):  # n-1 passes
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(arr)

if __name__ == "__main__":
    main()
