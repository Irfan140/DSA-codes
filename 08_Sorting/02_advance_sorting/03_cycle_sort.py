def main():
    arr = [4, 1, 6, 2, 5, 3]
    n = len(arr)
    
    # cycle sorting
    i = 0
    while i < n:
        correctIdx = arr[i] - 1
        if i == correctIdx:
            i += 1
        else:
            arr[i], arr[correctIdx] = arr[correctIdx], arr[i]
    
    for i in range(n):
        print(arr[i], end=" ")

if __name__ == "__main__":
    main()
