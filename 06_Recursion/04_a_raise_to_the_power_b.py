
def power(a, b):
    if b == 0: return 1
    return a * power(a, b - 1)

def main():
    a = int(input("Enter base: "))
    b = int(input("Enter power: "))

    print(power(a, b))

if __name__ == "__main__":
    main()