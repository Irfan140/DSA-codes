def main():
    n = int(input("Enter no. of rows: "))
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
