
def power(a, b):
    if b == 1: return a

    return power(a, b // 2) * power(a, b // 2)

def main():
    print(power(2, 3))

if __name__ == "__main__":
    main()

# TC, SC = O(logn)