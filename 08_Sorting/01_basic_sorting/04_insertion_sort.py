def main():
    n = int(input("Enter size: "))
    arr = list(map(int, input("Enter elements: ").split()))
    
    for i in range(1, n):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    
    # Print result
    for a in arr:
        print(a, end=" ")

if __name__ == "__main__":
    main()
