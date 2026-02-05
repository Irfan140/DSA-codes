# Converted from reverseFirstKElements.cpp

from collections import deque


def display(q: deque) -> None:
    n = len(q)
    for _ in range(n):
        x = q.popleft()
        print(x, end=" ")
        q.append(x)
    print()


def reverse_first_k(q: deque, k: int) -> None:
    n = len(q)
    if n == 0:
        return
    k = k % n
    st = []
    for _ in range(k):
        st.append(q.popleft())
    while st:
        q.append(st.pop())
    for _ in range(n - k):
        q.append(q.popleft())


def main():
    k = 3
    q = deque([1, 2, 3, 4, 5, 6])
    display(q)
    reverse_first_k(q, k)
    display(q)


if __name__ == "__main__":
    main()
