def solve(val1, val2, ch):
    if ch == '+':
        return val1 + val2
    elif ch == '-':
        return val1 - val2
    elif ch == '*':
        return val1 * val2
    else:
        return val1 // val2


def main():
    s = "-/*+79483"  # prefix expression
    val = []

    for i in range(len(s) - 1, -1, -1):
        # check if s[i] is a digit (0-9)
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            val.append(ord(s[i]) - 48)
        else:
            val1 = val[-1]
            val.pop()
            val2 = val[-1]
            val.pop()
            ans = solve(val1, val2, s[i])
            val.append(ans)

    print(val[-1])


if __name__ == "__main__":
    main()
