def stair(n):
    if n == 1 or n == 2: return n
    return stair(n - 1) + stair(n - 2)


def main():
    print(stair(5))


if __name__ == "__main__":
    main()
