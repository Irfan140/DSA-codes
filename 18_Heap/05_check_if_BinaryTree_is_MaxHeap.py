# Converted from isBinaryTreeMaxHEap.cpp

from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def is_max(root: Node) -> bool:
    if root is None:
        return True
    if root.left and root.val < root.left.val:
        return False
    if root.right and root.val < root.right.val:
        return False
    return is_max(root.left) and is_max(root.right)


def size_of_tree(root: Node) -> int:
    if root is None:
        return 0
    return 1 + size_of_tree(root.left) + size_of_tree(root.right)


def is_cbt(root: Node) -> bool:
    if root is None:
        return True
    q = deque([root])
    flag = False
    while q:
        temp = q.popleft()
        if temp.left:
            if flag:
                return False
            q.append(temp.left)
        else:
            flag = True
        if temp.right:
            if flag:
                return False
            q.append(temp.right)
        else:
            flag = True
    return True


def main():
    a = Node(20)
    b = Node(15)
    c = Node(10)
    d = Node(8)
    e = Node(11)
    f = None
    g = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    if is_cbt(a) and is_max(a):
        print("Tree is MaxHeap")
    else:
        print("Tree is not MaxHeap")


if __name__ == "__main__":
    main()
