def main():
    n = int(input("Enter size of array: "))
    arr = []
    print("Enter elements of array:")
    for i in range(n):
        arr.append(int(input()))
    
    x = int(input("Enter target: "))
    f = False
    
    for i in range(n):
        if arr[i] == x:
            f = True
            break
    
    if not f:
        print(f"{x} is not present in array")
    else:
        print(f"{x} is present in array")

if __name__ == "__main__":
    main()
