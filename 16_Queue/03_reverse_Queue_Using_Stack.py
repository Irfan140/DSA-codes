from collections import deque


def display(q: deque) -> None:
    """Print elements of the queue in order without changing its order."""
    n = len(q)
    for _ in range(n):
        x = q.popleft()
        print(x, end=" ")
        q.append(x)
    print()


def reverse(q: deque) -> None:
    """Reverse the contents of the queue using a stack (list)."""
    n = len(q)
    st = []
    for _ in range(n):
        st.append(q.popleft())
    while st:
        q.append(st.pop())


def main():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    reverse(q)
    display(q)


if __name__ == "__main__":
    main()
