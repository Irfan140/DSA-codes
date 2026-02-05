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

# constructing tree...
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

# boundary traversal....
def left_boundary(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    print(root.val, end=" ")
    left_boundary(root.left)
    if root.left is None:
        left_boundary(root.right)

def bottom_boundary(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val, end=" ")
    bottom_boundary(root.left)
    bottom_boundary(root.right)

def right_boundary(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    right_boundary(root.right)
    if root.right is None:
        right_boundary(root.left)
    print(root.val, end=" ")

def boundary(root):
    left_boundary(root)
    bottom_boundary(root)
    right_boundary(root.right)

def main():
    arr = [1, 2, 3, 4, 5, float('-inf'), 6, 7, float('-inf'), 8, float('-inf'), 9, 10, float('-inf'), 11, float('-inf'), 12, float('-inf'), 13, float('-inf'), 14, 15, 16, float('-inf'), 17, float('-inf'), float('-inf'), 18, float('-inf'), 19, float('-inf'), float('-inf'), float('-inf'), 20, 21, 22, 23, float('-inf'), 24, 25, 26, 27, float('-inf'), float('-inf'), 28, float('-inf'), float('-inf')]
    n = len(arr)
    root = construct(arr, n)
    
    boundary(root)

if __name__ == "__main__":
    main()
