def solve(val1, val2, ch):
    s = ""
    s += ch
    s += val1
    s += val2
    return s


def main():
    s = "79+4*8/3-"  # postfix expression
    val = []

    for i in range(len(s)):
        # check if s[i] is a digit (0-9)
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            val.append(str(ord(s[i]) - 48))
        else:
            val2 = val[-1]
            val.pop()
            val1 = val[-1]
            val.pop()
            ans = solve(val1, val2, s[i])
            val.append(ans)

    print(val[-1])
    # 7+9*4/8-3


if __name__ == "__main__":
    main()
