def fun(n):
    if n == 0:
        return 1
    print(n)
    fun(n - 1)

def main():
    n = int(input("Enter: "))
    fun(n)

if __name__ == "__main__":
    main()
