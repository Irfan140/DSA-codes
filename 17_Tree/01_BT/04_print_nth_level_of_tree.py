class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# To find hight of tree
def level(root):
    if root is None:
        return 0
    return 1 + max(level(root.left), level(root.right))


# # can be done by using preorder, postorder or inorder...here we are using preOrder
def nth_level(root, curr_level, desired_level):
    if root is None: return # base case
        
    if curr_level == desired_level:
        print(root.val, end=" ")  # work
        return
    
    nth_level(root.left, curr_level + 1, desired_level)  # call 1
    nth_level(root.right, curr_level + 1, desired_level)  # call 2

    # For printing in reverse order just write call 2 before call 1


# level order traversal (using DFS kind of)
def level_order(root):
    n = level(root)
    for i in range(1, n + 1):
        nth_level(root, 1, i) 
        print()

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
    
    nth_level(a, 1, 3)
    print()
    
    # level order traversal means printing every level of tree
    level_order(a)

if __name__ == "__main__":
    main()
