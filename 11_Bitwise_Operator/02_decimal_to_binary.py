def decimal_to_binary(num):
    result = ""
    while num > 0:
        if num % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result
        num = num // 2
    return result

def main():
    n = int(input("Enter number: "))
    print(decimal_to_binary(n))

if __name__ == "__main__":
    main()
