
def fibo(n):
    if n == 1 or n == 2: return 1

    return fibo(n - 1) + fibo(n - 2)

def main():
    # 1 1 2 3 5 8 13 21 ...
    n = int(input("Enter n: "))
    print(fibo(n))

if __name__ == "__main__":
    main()