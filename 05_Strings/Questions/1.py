# Converted from 1.cpp

def count_isolated_differences(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0
    if n == 2:
        return 1 if s[0] != s[1] else 0

    count = 0
    for i in range(n):
        if i == 0:
            if s[i] != s[i + 1]:
                count += 1
        elif i == n - 1:
            if s[i] != s[i - 1]:
                count += 1
        else:
            if s[i] != s[i - 1] and s[i] != s[i + 1]:
                count += 1
    return count


def main():
    s = "abaca"
    print(count_isolated_differences(s))


if __name__ == "__main__":
    main()
