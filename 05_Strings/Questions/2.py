# Converted from 2.cpp

def are_anagrams(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    s = "abc"
    t = "cba"
    print(are_anagrams(s, t))


if __name__ == "__main__":
    main()
