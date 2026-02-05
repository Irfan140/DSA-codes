def gcd(a, b):
    hcf = 1
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            hcf = i
            break
    return hcf

def main():
    a = int(input("Enter value: "))
    b = int(input("Enter value: "))
    print(gcd(a, b))

if __name__ == "__main__":
    main()
