class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order(root):
    if root is None:  # base case
        return
    print(root.val, end=" ")  # work
    pre_order(root.left)  # call 1
    pre_order(root.right)  # call 2

def in_order(root):
    if root is None:  # base case
        return
    in_order(root.left)  # call 1
    print(root.val, end=" ")  # work
    in_order(root.right)  # call 2

def post_order(root):
    if root is None:  # base case
        return
    post_order(root.left)  # call 1
    post_order(root.right)  # call 2
    print(root.val, end=" ")  # work

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    
    pre_order(a)
    print()
    in_order(a)
    print()
    post_order(a)

if __name__ == "__main__":
    main()
