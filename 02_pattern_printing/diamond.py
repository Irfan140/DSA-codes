def main():
    n = int(input("Enter no. of rows: "))
    nsp = n - 1
    nst = 1
    for i in range(1, 2 * n):
        for j in range(1, nsp + 1):
            print(" ", end="")
        
        if i < n:
            nsp -= 1
        else:
            nsp += 1
        
        for k in range(1, nst + 1):
            print("*", end="")
        
        if i < n:
            nst += 2
        else:
            nst -= 2
        
        print()

if __name__ == "__main__":
    main()
