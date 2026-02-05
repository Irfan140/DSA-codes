def main():
    n = int(input("Enter the number: "))
    a = 0
    b = 1
    sum_val = 0
    for i in range(1, n):
        sum_val = a + b
        a = b
        b = sum_val
    print(sum_val)

if __name__ == "__main__":
    main()
