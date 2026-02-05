"""Converted from 01_sub_set_of_string.cpp — original C++ removed."""

def main():
    def print_subsets(s: str, curr: str = "", idx: int = 0) -> None:
        if idx == len(s):
            print(curr)
            return
        print_subsets(s, curr + s[idx], idx + 1)
        print_subsets(s, curr, idx + 1)

    s = "abc"
    print_subsets(s)

if __name__ == "__main__":
    main()
