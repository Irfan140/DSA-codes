
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def construct(arr: list) -> Node:
    if not arr:
        return None
    root = Node(arr[0])
    from collections import deque
    q = deque([root])
    i = 1
    while q and i < len(arr):
        temp = q.popleft()
        # left
        if i < len(arr) and arr[i] is not None:
            temp.left = Node(arr[i])
            q.append(temp.left)
        i += 1
        # right
        if i < len(arr) and arr[i] is not None:
            temp.right = Node(arr[i])
            q.append(temp.right)
        i += 1
    return root


def level_order(root: Node) -> None:
    from collections import deque
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


def top_view(root: Node) -> None:
    from collections import deque, OrderedDict
    if not root:
        return
    q = deque([(root, 0)])
    m = {}
    while q:
        node, hd = q.popleft()
        if hd not in m:
            m[hd] = node.val
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    for hd in sorted(m.keys()):
        print(m[hd], end=" ")
    print()


def main():
    arr = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
    root = construct(arr)
    level_order(root)
    top_view(root)


if __name__ == "__main__":
    main()
