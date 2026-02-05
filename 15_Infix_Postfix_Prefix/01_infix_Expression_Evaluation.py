def priority(ch):
    if ch == '+' or ch == '-':
        return 1
    else:
        return 2  # for * and /


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
    s = "2+6*4/8-3"  # infix expression
    val = []
    op = []

    for i in range(len(s)):
        # check if s[i] is a digit (0-9)
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            val.append(ord(s[i]) - 48)
        else:
            # not a digit
            if len(op) == 0 or priority(s[i]) > priority(op[-1]):
                op.append(s[i])
            else:
                # priority(s[i])<=priority(op.top())
                while len(op) > 0 and priority(s[i]) <= priority(op[-1]):
                    ch = op[-1]
                    op.pop()
                    val2 = val[-1]
                    val.pop()
                    val1 = val[-1]
                    val.pop()
                    ans = solve(val1, val2, ch)
                    val.append(ans)
                op.append(s[i])

    # After all thsese the op stack may still have values
    # so make it empty
    while len(op) > 0:
        ch = op[-1]
        op.pop()
        val2 = val[-1]
        val.pop()
        val1 = val[-1]
        val.pop()
        ans = solve(val1, val2, ch)
        val.append(ans)

    print(val[-1])


if __name__ == "__main__":
    main()
