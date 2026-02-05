def binary_to_decimal(binary):
    n = len(binary)
    result = 0
    for i in range(n - 1, -1, -1):
        ch = binary[i]
        num = int(ch)
        result += num * (1 << (n - i - 1))
    return result

def main():
    str_binary = input("Enter binary number: ")
    print(binary_to_decimal(str_binary))

if __name__ == "__main__":
    main()
