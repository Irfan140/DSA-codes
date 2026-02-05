# Two elements of an array a, a[i] and a[j] form an inversion if a[i]>a[j] and i<j.
# Given an array of integers, find the inversion count in the array

c = 0

def inversion(a, b):
    count = 0
    i = 0  # corresponds a
    j = 0  # corresponds b
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            count += len(a) - i
            j += 1
        else:
            # a[i] <= b[j]
            i += 1
    return count

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
    global c
    n = len(v)
    if n == 1:
        return  # base case
    
    n1 = n // 2
    n2 = n - n // 2
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
    
    # Before merging count the inversions
    c += inversion(a, b)
    
    # merge sorted array
    merge(a, b, v)

def main():
    global c
    arr = [5, 1, 3, 0, 4, 9, 6]
    v = arr[:]  # copy array to list
    mergeSort(v)
    print(c)

if __name__ == "__main__":
    main()
