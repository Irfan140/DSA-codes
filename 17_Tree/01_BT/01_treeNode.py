class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

if __name__ == "__main__":
    main()
