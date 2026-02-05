
from collections import deque


def reorder_queue(q: deque) -> None:
    """Interleave first and second halves of an even-sized queue using one stack."""
    n = len(q)
    if n % 2 != 0:
        raise ValueError("Queue size must be even for this algorithm")

    st = []

    # Step 1: move first half to stack
    while len(q) > n // 2:
        st.append(q.popleft())

    # Step 2: move stack back to queue (reverses that half)
    while st:
        q.append(st.pop())

    # Step 3: move first half (which are the second half of original) to stack
    while len(q) > n // 2:
        st.append(q.popleft())

    # Step 4: interleave elements from stack and queue
    while st:
        q.append(st.pop())       # push one from stack
        q.append(q.popleft())    # then one from queue

    # Step 5: reverse final order by moving to stack and back
    while q:
        st.append(q.popleft())
    while st:
        q.append(st.pop())


def main():
    q = deque(range(1, 9))
    reorder_queue(q)
    # print final queue
    n = len(q)
    for _ in range(n):
        print(q[0], end=" ")
        q.append(q.popleft())
    print()


if __name__ == "__main__":
    main()
