from collections import deque

def main():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)

    print(q[0])  # front
    print(q[-1])  # back

    q.popleft()
    
    print(q[0])  # front
    print(q[-1])  # back

if __name__ == "__main__":
    main()
