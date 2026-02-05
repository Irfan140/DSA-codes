def partition(arr, si, ei):
    pivotElement = arr[(si + ei) // 2]
    count = 0
    for i in range(si, ei + 1):
        if i == (si + ei) // 2:
            continue
        if arr[i] <= pivotElement:
            count += 1
    
    pivotIdx = count + si
    arr[(si + ei) // 2], arr[pivotIdx] = arr[pivotIdx], arr[(si + ei) // 2]
    
    i = si
    j = ei
    while i < pivotIdx and j > pivotIdx:
        if arr[i] <= pivotElement:
            i += 1
        if arr[j] > pivotElement:
            j -= 1
        elif arr[i] > pivotElement and arr[j] <= pivotElement:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    return pivotIdx

def quickSort(arr, si, ei):
    if si >= ei:
        return
    
    pi = partition(arr, si, ei)
    quickSort(arr, si, pi - 1)
    quickSort(arr, pi + 1, ei)

def main():
    arr = [5, 1, 8, 2, 7, 6, 3, 4]
    n = len(arr)
    quickSort(arr, 0, n - 1)  # array, starting index, last index
    
    for i in range(n):
        print(arr[i], end=" ")

if __name__ == "__main__":
    main()
