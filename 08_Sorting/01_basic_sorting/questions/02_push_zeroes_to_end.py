# Push zeroes to end while maintaining the relative orders of elements

def main():
    n = int(input("Enter size: "))
    arr = list(map(int, input("Enter elements: ").split()))
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] == 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    for i in range(n):
        print(arr[i], end=" ")

if __name__ == "__main__":
    main()
