def fun(a, n):
    if a > n:
        return
    print(a)
    fun(a + 1, n)

def main():
    n = int(input("Enter: "))
    fun(1, n)

if __name__ == "__main__":
    main()
