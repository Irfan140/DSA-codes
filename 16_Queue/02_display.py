from collections import deque

def display(q):
    n = len(q)
    for i in range(n):
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

if __name__ == "__main__":
    main()
