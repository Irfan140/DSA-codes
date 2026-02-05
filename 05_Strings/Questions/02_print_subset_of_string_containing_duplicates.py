

def main():
    def store_subsets(ans: str, original: str, v: list, flag: bool) -> None:
        if original == "":
            v.append(ans)
            return

        ch = original[0]
        if len(original) == 1:
            if flag:
                store_subsets(ans + ch, original[1:], v, True)
            store_subsets(ans, original[1:], v, True)
            return

        dh = original[1]
        if ch == dh:
            if flag:
                store_subsets(ans + ch, original[1:], v, True)
            store_subsets(ans, original[1:], v, False)
        else:
            if flag:
                store_subsets(ans + ch, original[1:], v, True)
            store_subsets(ans, original[1:], v, True)

    s = "aab"
    s = ''.join(sorted(s))
    v = []
    store_subsets("", s, v, True)
    for x in v:
        print(x)

if __name__ == "__main__":
    main()
