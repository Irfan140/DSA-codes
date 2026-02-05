def helper(ans, original, v):
    if original == "":
        v.append(ans)
        return
    ch = original[0]
    helper(ans + ch, original[1:], v)
    helper(ans, original[1:], v)

def main():
    s = input("Enter string: ")
    v = []
    helper("", s, v)
    for e in v:
        print(e)

if __name__ == "__main__":
    main()
