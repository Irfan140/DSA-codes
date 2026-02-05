# Converted from 04_permutation.cpp

from itertools import permutations


def main():
    s = input().strip()
    seen = set()
    for p in permutations(s):
        perm = ''.join(p)
        if perm not in seen:
            print(perm)
            seen.add(perm)


if __name__ == "__main__":
    main()
