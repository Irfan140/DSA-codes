# in case when no. of element is even we take left middle as middle
# time complexity is O(logn)

def main():
    arr = list(map(int, input("Enter elements: ").split()))
    n = len(arr)
    
    x = int(input("Enter target: "))
    
    low = 0
    high = n - 1
    
    flag = True
    while low <= high:
        mid = low + (high - low) // 2  # For safety
        if arr[mid] == x:
            flag = False
            break
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    
    if flag:
        print(f"{x} is not present in array")
    else:
        print(f"{x} is present in array")

if __name__ == "__main__":
    main()
