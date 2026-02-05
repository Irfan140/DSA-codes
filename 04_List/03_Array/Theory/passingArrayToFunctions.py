def display(a, size):
    for i in range(size - 1):
        print(a[i], end=" ")
    print()
    return

def change(b, size):
    b[0] = 100

def main():
    arr = [1, 2, 3, 4, 5]
    size = len(arr)
    display(arr, size)
    change(arr, size)
    display(arr, size)

if __name__ == "__main__":
    main()
