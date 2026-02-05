def main():
    n = int(input("Enter size: "))
    arr = list(map(int, input("Enter elements: ").split()))
    
    for i in range(n - 1):
        min_val = float('inf')
        idx = -1
        # minimum element calculation
        for j in range(i, n):
            if arr[j] < min_val:
                min_val = arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    
    # Print result
    print(arr)

if __name__ == "__main__":
    main()
