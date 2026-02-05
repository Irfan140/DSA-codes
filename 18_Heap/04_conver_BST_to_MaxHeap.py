# Converted from converBSTtoMaxHeap.cpp

from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def inorder_reverse(root: Node, arr: list) -> None:
    if not root:
        return
    inorder_reverse(root.right, arr)
    arr.append(root.val)
    inorder_reverse(root.left, arr)


def preorder_assign(root: Node, arr: list, i: list) -> None:
    if not root:
        return
    root.val = arr[i[0]]
    i[0] += 1
    preorder_assign(root.left, arr, i)
    preorder_assign(root.right, arr, i)


def level_order(root: Node) -> None:
    if not root:
        return
    q = deque([root])
    while q:
        temp = q.popleft()
        print(temp.val, end=" ")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    print()


def main():
    a = Node(10)
    b = Node(5)
    c = Node(16)
    d = Node(1)
    e = Node(8)
    f = Node(12)
    g = Node(20)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    arr = []
    inorder_reverse(a, arr)
    level_order(a)
    i = [0]
    preorder_assign(a, arr, i)  # BST -> MaxHeap
    level_order(a)


if __name__ == "__main__":
    main()
