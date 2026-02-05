def main():
    n = int(input("Enter size of array: "))
    arr = []
    print("Enter elements of array:")
    arr = list(map(int, input().split()))
    
    max_val = float('-inf')
    smax = float('-inf')
    
    for i in range(n):
        if max_val < arr[i]:
            max_val = arr[i]
    
    for i in range(n):
        if arr[i] != max_val and smax < arr[i]:
            smax = arr[i]
    
    print(f"Second largest is {smax}")

if __name__ == "__main__":
    main()
