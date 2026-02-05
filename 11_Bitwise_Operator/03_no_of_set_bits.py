def count_set_bits(n):
    count = 0
    while n > 0:
        count += 1
        n = n & (n - 1)
    return count

def main():
    n = int(input())
    print(count_set_bits(n))

if __name__ == "__main__":
    main()
