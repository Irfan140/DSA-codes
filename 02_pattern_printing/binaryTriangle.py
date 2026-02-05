def main():
    n = int(input("Enter no. of rows: "))
    a = 5  # we can initialise by any value
    for i in range(1, n + 1):
        if i % 2 != 0:  # row no. odd
            a = 1
        else:  # row no. even
            a = 0
        
        for j in range(1, i + 1):
            print(a, end=" ")
            # flipping
            if a == 1:
                a = 0
            else:
                a = 1
        print()

if __name__ == "__main__":
    main()
