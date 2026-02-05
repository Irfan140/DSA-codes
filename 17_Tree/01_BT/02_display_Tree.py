class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# display
def display(root):
    if root is None: return
        
    print(root.val, end=" ")
    display(root.left)
    display(root.right)

# sum of nodes value
def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

# size of tree
def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# max value of node
def max_node(root):
    if root is None:
        return float('-inf')
    return max(root.val, max(max_node(root.left), max_node(root.right)))

# level of tree (height)
def level(root):
    if root is None:
        return 0
    return 1 + max(level(root.left), level(root.right))

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
    
    display(a)
    print()

    print(f"Sum of nodes is: {sum_tree(a)}")
    print(f"Max node val is {size(a)}")
    print(f"Height of tree is {level(a)}")

if __name__ == "__main__":
    main()
