def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n)

def main():
    n = int(input("Enter: "))
    fun(n)

if __name__ == "__main__":
    main()
