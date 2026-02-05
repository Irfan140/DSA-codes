def main():
    arr = [4, 3, 2, 1]
    n = 4
    
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:  # Swap did not happen
            break
    
    print(arr)

if __name__ == "__main__":
    main()
