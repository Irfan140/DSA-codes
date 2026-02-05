from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        temp = q.popleft()
        print(temp.val, end=" ")
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
    print()

def construct(arr, n):
    root = Node(arr[0])
    q = deque()
    q.append(root)
    i = 1
    j = 2
    while len(q) > 0 and i < n:
        temp = q.popleft()
        if arr[i] != float('-inf'):
            l = Node(arr[i])
        else:
            l = None
        if j < n and arr[j] != float('-inf'):
            r = Node(arr[j])
        else:
            r = None
        temp.left = l
        temp.right = r
        
        if l is not None:
            q.append(l)
        if r is not None:
            q.append(r)
        
        i += 2
        j += 2
    return root

def main():
    arr = [1, 2, 3, 4, 5, float('-inf'), 6, float('-inf'), float('-inf'), 7, 8, 9]
    n = len(arr)
    root = construct(arr, n)
    
    level_order(root)

if __name__ == "__main__":
    main()
