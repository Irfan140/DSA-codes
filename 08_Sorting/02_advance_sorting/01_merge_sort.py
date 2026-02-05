def merge(a, b, res):
    i = 0  # for a
    j = 0  # for b
    k = 0  # for res
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res[k] = a[i]
            k += 1
            i += 1
        else:
            # b[j] <= a[i]
            res[k] = b[j]
            k += 1
            j += 1
    
    if i == len(a):
        while j < len(b):
            res[k] = b[j]
            k += 1
            j += 1
    
    if j == len(b):  # b is at end
        while i < len(a):
            res[k] = a[i]
            k += 1
            i += 1

def mergeSort(v):
    n = len(v)
    if n == 1:
        return  # base case
    
    n1 = n // 2
    n2 = n - n // 2
    
    # Creates a list of size n1 with Every element is initialized to 0
    a = [0] * n1
    b = [0] * n2
    
    # copy pasting
    for i in range(n1):
        a[i] = v[i]
    for i in range(n2):
        b[i] = v[i + n1]
    
    # Magic -> recursion
    mergeSort(a)
    mergeSort(b)
    
    # merge sorted array
    merge(a, b, v)

def main():
    arr = list(map(int, input("Enter elements: ").split()))
    v = arr[:]  # all elements in array gets copied to list
    mergeSort(v)
    
    print(v)

if __name__ == "__main__":
    main()
