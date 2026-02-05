# Converted from removeAtEvenIndex.cpp

from collections import deque


def remove_even_index(q: deque) -> None:
    n = len(q)
    for i in range(n):
        if i % 2 == 0:
            q.popleft()
        else:
            x = q.popleft()
            q.append(x)


def display(q: deque) -> None:
    n = len(q)
    for _ in range(n):
        x = q.popleft()
        print(x, end=" ")
        q.append(x)
    print()


def main():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    display(q)
    remove_even_index(q)
    display(q)


if __name__ == "__main__":
    main()
