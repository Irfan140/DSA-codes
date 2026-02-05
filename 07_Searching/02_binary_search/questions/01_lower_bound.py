# Lower bound returns the index of the first element ≥ target

def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low



def main():
    arr = list(map(int, input("Enter elements: ").split()))
    
    target = int(input("Enter target: "))

    idx = lower_bound(arr, target)

    print(arr[idx])



if __name__ == "__main__":
    main()

